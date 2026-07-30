import json
from pathlib import Path
import numpy as np

with open("method_out.json", "r") as f:
    data = json.load(f)

naive_mses, static_mses, unnorm_mses, self_norm_mses = [], [], [], []

for ds in data["datasets"]:
    for res in ds["results"]:
        m = res["metrics"]
        naive_mses.append(m["naive_persistence"]["mse"])
        static_mses.append(m["static_ma3"]["mse"])
        unnorm_mses.append(m["unnormalized_psama"]["mse"])
        self_norm_mses.append(m["self_normalized_psama"]["mse"])

print(f"Mean MSE - Naive Persistence: {np.mean(naive_mses):.4f}")
print(f"Mean MSE - Static MA(3): {np.mean(static_mses):.4f}")
print(f"Mean MSE - Unnormalized PSAMA: {np.mean(unnorm_mses):.4f}")
print(f"Mean MSE - Self-Normalized PSAMA: {np.mean(self_norm_mses):.4f}")
