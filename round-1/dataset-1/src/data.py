import json
import os

workspace = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"
input_path = os.path.join(workspace, "temp/datasets/synthetic_time_series.json")

with open(input_path, "r") as f:
    raw_data = json.load(f)

datasets_group = []
chunk_size = len(raw_data) // 10

for i in range(10):
    chunk = raw_data[i * chunk_size : (i + 1) * chunk_size]
    examples = []
    for item in chunk:
        examples.append({
            "input": json.dumps(item["input_series"]),
            "output": json.dumps(item["clean_trajectory"]),
            "metadata_id": item["id"],
            "metadata_process_type": item["process_type"],
            "metadata_length": item["length"],
            "metadata_noise_level": item["noise_level"]
        })
    datasets_group.append({
        "dataset": f"synthetic_time_series_group_{i+1}",
        "examples": examples
    })

full_data = {"datasets": datasets_group}

full_out = os.path.join(workspace, "full_data_out.json")
with open(full_out, "w") as f:
    json.dump(full_data, f, indent=2)

mini_datasets = []
for ds in datasets_group:
    mini_datasets.append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:3]
    })
mini_data = {"datasets": mini_datasets}
with open(os.path.join(workspace, "mini_data_out.json"), "w") as f:
    json.dump(mini_data, f, indent=2)

preview_datasets = []
for ds in datasets_group:
    preview_datasets.append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:10]
    })
preview_data = {"datasets": preview_datasets}
with open(os.path.join(workspace, "preview_data_out.json"), "w") as f:
    json.dump(preview_data, f, indent=2)

print("Generated full, mini, and preview datasets across 10 dataset groups successfully.")
