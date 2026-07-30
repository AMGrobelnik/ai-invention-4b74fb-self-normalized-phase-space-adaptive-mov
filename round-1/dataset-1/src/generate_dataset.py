import numpy as np
import json
import os

workspace = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_dataset_1"
os.makedirs(workspace, exist_ok=True)
os.makedirs(os.path.join(workspace, "temp/datasets"), exist_ok=True)

np.random.seed(42)
data = []
noise_levels = [0.01, 0.05, 0.1, 0.2, 0.5]

for i in range(1000):
    length = np.random.randint(50, 101)
    noise_level = np.random.choice(noise_levels)
    process_type = np.random.choice(["ou", "sine"])
    
    if process_type == "ou":
        # Ornstein-Uhlenbeck process
        theta = 0.1
        mu = 0.0
        sigma = 0.2
        dt = 1.0
        x = np.zeros(length)
        x[0] = np.random.normal(0, 1)
        for t in range(1, length):
            x[t] = x[t-1] + theta * (mu - x[t-1]) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1)
        clean = x
    else:
        # Sine wave
        freq = np.random.uniform(0.05, 0.2)
        phase = np.random.uniform(0, 2 * np.pi)
        t = np.arange(length)
        clean = np.sin(2 * np.pi * freq * t + phase)
        
    noise = np.random.normal(0, noise_level, length)
    noisy = clean + noise
    
    item = {
        "id": i,
        "process_type": process_type,
        "length": length,
        "noise_level": float(noise_level),
        "clean_trajectory": clean.tolist(),
        "input_series": noisy.tolist()
    }
    data.append(item)

out_path = os.path.join(workspace, "temp/datasets/synthetic_time_series.json")
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(data)} synthetic time series sequences at {out_path}")
