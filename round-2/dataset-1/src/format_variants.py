# /// script
# dependencies = []
# ///

import json

full_path = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json"
with open(full_path, "r") as f:
    data = json.load(f)

# Select top 4 datasets based on variety (OU low/high noise, noisy sine low/high noise)
selected_names = {
    "ou_process_low_noise",
    "ou_process_high_noise",
    "noisy_sine_low_noise",
    "noisy_sine_high_noise"
}

filtered_datasets = [ds for ds in data["datasets"] if ds["dataset"] in selected_names]

preview_data = {
    "datasets": [
        {
            "dataset": ds["dataset"],
            "examples": ds["examples"][:5] # first 5 examples
        }
        for ds in filtered_datasets
    ]
}

mini_data = {
    "datasets": [
        {
            "dataset": ds["dataset"],
            "examples": ds["examples"][:20] # first 20 examples
        }
        for ds in filtered_datasets
    ]
}

final_selected_data = {
    "datasets": filtered_datasets
}

# Save full_data_out.json as filtered version
with open("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json", "w") as f:
    json.dump(final_selected_data, f, indent=2)

with open("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
    json.dump(preview_data, f, indent=2)

with open("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
    json.dump(mini_data, f, indent=2)

print("Generated full, preview, and mini datasets successfully.")
