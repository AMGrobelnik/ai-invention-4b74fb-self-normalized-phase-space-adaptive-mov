import os
import json
import numpy as np

os.makedirs("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets", exist_ok=True)

# Generate synthetic time series datasets for Phase-Space Adaptive Moving Average
np.random.seed(42)

# 1. Ornstein-Uhlenbeck process (mean reverting)
def generate_ou(n=1000, theta=0.15, mu=0.0, sigma=0.2):
    dt = 1.0
    x = np.zeros(n)
    x[0] = mu
    for i in range(1, n):
        x[i] = x[i-1] + theta * (mu - x[i-1]) * dt + sigma * np.sqrt(dt) * np.random.randn()
    return x

# 2. Noisy Sine Wave
def generate_noisy_sine(n=1000, freq=0.05, noise=0.1):
    t = np.arange(n)
    return np.sin(2 * np.pi * freq * t) + noise * np.random.randn(n)

datasets = {
    "ou_process_low_noise": generate_ou(2000, sigma=0.1).tolist(),
    "ou_process_high_noise": generate_ou(2000, sigma=0.5).tolist(),
    "noisy_sine_low_noise": generate_noisy_sine(2000, noise=0.05).tolist(),
    "noisy_sine_high_noise": generate_noisy_sine(2000, noise=0.4).tolist(),
    "random_walk_drift": np.cumsum(0.01 + 0.1 * np.random.randn(2000)).tolist(),
    "regime_switching_ts": np.concatenate([np.sin(np.linspace(0, 10, 500)) + 0.1*np.random.randn(500),
                                          np.cumsum(0.05 * np.random.randn(1000)),
                                          np.sin(np.linspace(0, 20, 500)) + 0.5*np.random.randn(500)]).tolist(),
    "garch_like_volatility": (np.random.randn(2000) * np.cumprod(1 + 0.01 * np.random.randn(2000))).tolist(),
    "trend_stationary": (np.linspace(0, 5, 2000) + generate_ou(2000, sigma=0.2)).tolist()
}

for name, data in datasets.items():
    path = f"/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets/{name}.json"
    with open(path, "w") as f:
        json.dump({"dataset_name": name, "length": len(data), "values": data}, f)

print(f"Successfully generated {len(datasets)} synthetic datasets in temp/datasets/")
