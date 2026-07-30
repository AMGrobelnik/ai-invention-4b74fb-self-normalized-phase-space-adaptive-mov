# /// script
# dependencies = ["numpy"]
# ///

import os
import json
import numpy as np

temp_dir = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets"
files = [f for f in os.listdir(temp_dir) if f.endswith(".json")]

datasets_list = []

for filename in files:
    path = os.path.join(temp_dir, filename)
    with open(path, "r") as f:
        content = json.load(f)
    
    dataset_name = content.get("dataset_name", filename.replace(".json", ""))
    values = content.get("values", [])
    
    examples = []
    # For time series prediction, each example can be a sliding window or consecutive points
    # Let's create examples where input is historical window and output is next value
    window_size = 10
    for i in range(len(values) - window_size):
        window = values[i:i+window_size]
        target = values[i+window_size]
        
        example = {
            "input": json.dumps({"history": window}),
            "output": str(target),
            "metadata_fold": 0 if i < len(values) * 0.8 else 1,
            "metadata_row_index": i,
            "metadata_task_type": "regression"
        }
        examples.append(example)
    
    datasets_list.append({
        "dataset": dataset_name,
        "examples": examples
    })

output_data = {
    "datasets": datasets_list
}

out_path = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json"
with open(out_path, "w") as f:
    json.dump(output_data, f, indent=2)

print(f"Successfully standardized {len(datasets_list)} datasets into {out_path}")
