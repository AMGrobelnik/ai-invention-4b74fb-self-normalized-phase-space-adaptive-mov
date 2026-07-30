import json
import numpy as np

def main():
    data_path = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json"
    with open(data_path, "r") as f:
        data = json.load(f)
    
    source_dataset = data["datasets"][0]
    examples = source_dataset["examples"]
    
    all_actuals = []
    all_preds = []
    
    new_examples = []
    for ex in examples:
        noise_level = ex["metadata_noise_level"]
        actuals = np.array(json.loads(ex["input"]))
        preds = np.array(json.loads(ex["output"]))
        
        mse = float(np.mean((actuals - preds) ** 2))
        
        naive_preds = np.roll(actuals, 1)
        naive_preds[0] = actuals[0]
        naive_mse = float(np.mean((actuals - naive_preds) ** 2))
        
        all_actuals.extend(actuals)
        all_preds.extend(preds)
        
        new_ex = {
            "input": ex["input"],
            "output": ex["output"],
            "metadata_id": ex.get("metadata_id", 0),
            "metadata_process_type": ex.get("metadata_process_type", "ou"),
            "metadata_length": ex.get("metadata_length", len(actuals)),
            "metadata_noise_level": noise_level,
            "predict_adaptive_ma": ex["output"],
            "eval_mse": mse,
            "eval_naive_mse": naive_mse
        }
        new_examples.append(new_ex)
        
    overall_ma_mse = float(np.mean((np.array(all_actuals) - np.array(all_preds)) ** 2))
    
    results = {
        "metrics_agg": {
            "overall_ma_mse": overall_ma_mse
        },
        "datasets": [
            {
                "dataset": source_dataset.get("dataset", "synthetic_time_series"),
                "examples": new_examples
            }
        ]
    }
    
    out_path = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1/eval_out.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
        
    print("Evaluation JSON successfully generated with schema compliance.")

if __name__ == "__main__":
    main()
