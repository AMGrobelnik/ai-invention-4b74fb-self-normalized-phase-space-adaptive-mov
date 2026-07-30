import json
from pathlib import Path

with open("method_out.json", "r") as f:
    data = json.load(f)

# Save full_method_out.json
Path("full_method_out.json").write_text(json.dumps(data, indent=2))

# Generate mini version (~3 examples per dataset)
mini_datasets = []
for ds in data["datasets"]:
    mini_datasets.append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:3]
    })
mini_data = {"metadata": data.get("metadata", {}), "datasets": mini_datasets}
Path("mini_method_out.json").write_text(json.dumps(mini_data, indent=2))

# Generate preview version (~10 examples per dataset)
preview_datasets = []
for ds in data["datasets"]:
    preview_datasets.append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:10]
    })
preview_data = {"metadata": data.get("metadata", {}), "datasets": preview_datasets}
Path("preview_method_out.json").write_text(json.dumps(preview_data, indent=2))

print("Generated full_method_out.json, mini_method_out.json, and preview_method_out.json successfully.")
