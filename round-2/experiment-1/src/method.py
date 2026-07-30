import json
import numpy as np
from pathlib import Path
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    logger.info("Starting Self-Normalized Phase-Space Adaptive Moving Average evaluation adhering to exp_gen_sol_out schema")
    
    data_path = Path("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json")
    if not data_path.exists():
        data_path = Path("full_data_out.json")
    
    with open(data_path, "r") as f:
        data = json.load(f)
    
    all_datasets = []
    
    def rolling_mad(series, window=5):
        mad = np.zeros_like(series)
        for i in range(len(series)):
            start = max(0, i - window + 1)
            chunk = series[start:i+1]
            med = np.median(chunk)
            mad[i] = np.median(np.abs(chunk - med)) + 1e-8
        return mad

    for ds in data["datasets"]:
        ds_name = ds["dataset"]
        logger.info(f"Processing dataset group: {ds_name}")
        
        examples_out = []
        for ex in ds["examples"]:
            inp = json.loads(ex["input"])
            out = json.loads(ex["output"])
            
            # Models predictions
            pred_naive = [inp[0]] + inp[:-1]
            
            pred_static_ma = []
            for i in range(len(inp)):
                start = max(0, i - 2)
                pred_static_ma.append(float(np.mean(inp[start:i+1])))
                
            pred_unnorm_psama = []
            for i in range(len(inp)):
                if i == 0:
                    pred_unnorm_psama.append(inp[0])
                    continue
                grad = abs(inp[i] - inp[i-1])
                w = int(np.clip(round(3 / (1.0 + grad * 5.0)), 1, 5))
                start = max(0, i - w + 1)
                pred_unnorm_psama.append(float(np.mean(inp[start:i+1])))
                
            mad_series = rolling_mad(np.array(inp), window=5)
            pred_self_norm_psama = []
            for i in range(len(inp)):
                if i == 0:
                    pred_self_norm_psama.append(inp[0])
                    continue
                grad = abs(inp[i] - inp[i-1])
                norm_grad = grad / mad_series[i]
                w = int(np.clip(round(3 / (1.0 + norm_grad * 5.0)), 1, 5))
                start = max(0, i - w + 1)
                pred_self_norm_psama.append(float(np.mean(inp[start:i+1])))
                
            example_entry = {
                "input": ex["input"],
                "output": ex["output"],
                "metadata_id": str(ex["metadata_id"]),
                "metadata_process_type": str(ex["metadata_process_type"]),
                "metadata_noise_level": str(ex["metadata_noise_level"]),
                "predict_naive_persistence": json.dumps(pred_naive),
                "predict_static_ma3": json.dumps(pred_static_ma),
                "predict_unnormalized_psama": json.dumps(pred_unnorm_psama),
                "predict_self_normalized_psama": json.dumps(pred_self_norm_psama)
            }
            examples_out.append(example_entry)
            
        all_datasets.append({
            "dataset": ds_name,
            "examples": examples_out
        })
        
    output_data = {
        "metadata": {
            "experiment": "Self-Normalized Phase-Space Adaptive Moving Average"
        },
        "datasets": all_datasets
    }
    
    out_path = Path("method_out.json")
    out_path.write_text(json.dumps(output_data, indent=2))
    logger.info(f"Successfully saved experiment results to {out_path}")

if __name__ == "__main__":
    main()
