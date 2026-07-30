#!/usr/bin/env python3
"""Evaluation script for Normalized PSAMA Statistical Rigor and Error Analysis conforming strictly to exp_eval_sol_out schema."""

import json
import sys
from pathlib import Path
import numpy as np
from scipy import stats
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    logger.info("Starting evaluation of adaptive moving average forecasting vs baselines.")
    
    dep_path = Path("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/full_method_out.json")
    if not dep_path.exists():
        dep_path = Path("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method_out.json")
    
    logger.info(f"Loading data from {dep_path}")
    data = json.loads(dep_path.read_text())
    
    dep_examples = data["datasets"][0]["examples"]
    logger.info(f"Loaded {len(dep_examples)} examples.")
    
    actuals = []
    pred_adap = []
    pred_stat = []
    pred_naiv = []
    
    for ex in dep_examples:
        actuals.append(float(ex["output"]))
        pred_adap.append(float(ex["predict_adaptive_ma"]))
        pred_stat.append(float(ex["predict_static_ma"]))
        pred_naiv.append(float(ex["predict_naive"]))
        
    actuals = np.array(actuals)
    pred_adap = np.array(pred_adap)
    pred_stat = np.array(pred_stat)
    pred_naiv = np.array(pred_naiv)
    
    def compute_metrics(y_true, y_pred):
        mse = float(np.mean((y_true - y_pred) ** 2))
        rmse = float(np.sqrt(mse))
        mae = float(np.mean(np.abs(y_true - y_pred)))
        return mse, rmse, mae
        
    mse_adap, rmse_adap, mae_adap = compute_metrics(actuals, pred_adap)
    mse_stat, rmse_stat, mae_stat = compute_metrics(actuals, pred_stat)
    mse_naiv, rmse_naiv, mae_naiv = compute_metrics(actuals, pred_naiv)
    
    # Statistical tests (Wilcoxon signed-rank test on squared errors)
    se_adap = (actuals - pred_adap) ** 2
    se_stat = (actuals - pred_stat) ** 2
    se_naiv = (actuals - pred_naiv) ** 2
    
    wilcoxon_stat_vs_adap = stats.wilcoxon(se_stat, se_adap)
    wilcoxon_naiv_vs_adap = stats.wilcoxon(se_naiv, se_adap)
    
    eval_examples = []
    for i, ex in enumerate(dep_examples):
        eval_ex = {
            "input": ex["input"],
            "output": ex["output"],
            "predict_adaptive_ma": ex["predict_adaptive_ma"],
            "predict_static_ma": ex["predict_static_ma"],
            "predict_naive": ex["predict_naive"],
            "eval_adaptive_mse": float(se_adap[i]),
            "eval_static_mse": float(se_stat[i]),
            "eval_naive_mse": float(se_naiv[i])
        }
        eval_examples.append(eval_ex)
        
    eval_result = {
        "metadata": {
            "evaluation_name": "Normalized PSAMA Statistical Rigor and Error Analysis",
            "description": "Comprehensive evaluation of normalized PSAMA against static moving average and naive persistence across multiple error metrics and statistical significance tests.",
            "wilcoxon_static_vs_adaptive_statistic": float(wilcoxon_stat_vs_adap.statistic),
            "wilcoxon_static_vs_adaptive_pvalue": float(wilcoxon_stat_vs_adap.pvalue),
            "wilcoxon_naive_vs_adaptive_statistic": float(wilcoxon_naiv_vs_adap.statistic),
            "wilcoxon_naive_vs_adaptive_pvalue": float(wilcoxon_naiv_vs_adap.pvalue)
        },
        "metrics_agg": {
            "mse_adaptive": mse_adap,
            "rmse_adaptive": rmse_adap,
            "mae_adaptive": mae_adap,
            "mse_static": mse_stat,
            "rmse_static": rmse_stat,
            "mae_static": mae_stat,
            "mse_naive": mse_naiv,
            "rmse_naive": rmse_naiv,
            "mae_naive": mae_naiv
        },
        "datasets": [
            {
                "dataset": "ornstein_uhlenbeck_synthetic",
                "examples": eval_examples
            }
        ]
    }
    
    out_dir = Path("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1/results")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    eval_out_path = out_dir / "eval_out.json"
    eval_out_path.write_text(json.dumps(eval_result, indent=2))
    logger.info(f"Saved eval_out.json to {eval_out_path}")
    
    # Also generate mini, preview, and full versions
    full_path = out_dir / "full_eval_out.json"
    full_path.write_text(json.dumps(eval_result, indent=2))
    
    mini_result = eval_result.copy()
    mini_result["datasets"] = [{
        "dataset": "ornstein_uhlenbeck_synthetic",
        "examples": eval_examples[:3]
    }]
    mini_path = out_dir / "mini_eval_out.json"
    mini_path.write_text(json.dumps(mini_result, indent=2))
    
    preview_result = mini_result.copy()
    preview_path = out_dir / "preview_eval_out.json"
    preview_path.write_text(json.dumps(preview_result, indent=2))
    
    # Also copy eval_out.json to workspace root for convenience
    Path("eval_out.json").write_text(json.dumps(eval_result, indent=2))
    Path("full_eval_out.json").write_text(json.dumps(eval_result, indent=2))
    Path("mini_eval_out.json").write_text(json.dumps(mini_result, indent=2))
    Path("preview_eval_out.json").write_text(json.dumps(preview_result, indent=2))
    
    logger.info("Saved full, mini, and preview eval outputs successfully.")

if __name__ == "__main__":
    main()
