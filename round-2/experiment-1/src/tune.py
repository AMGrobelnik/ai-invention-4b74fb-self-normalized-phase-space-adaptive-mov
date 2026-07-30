import json
from pathlib import Path
import numpy as np

with open("method_out.json", "r") as f:
    data = json.load(f)

for scale_factor in [0.5, 1.0, 2.0, 5.0]:
    # Let's test different parameterizations on group 1
    ds = data["datasets"][0]
    mses = []
    with open("/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json") as f_full:
        full_data = json.load(f_full)
    exs = full_data["datasets"][0]["examples"]
    
    def rolling_mad(series, window=5):
        mad = np.zeros_like(series)
        for i in range(len(series)):
            start = max(0, i - window + 1)
            chunk = series[start:i+1]
            med = np.median(chunk)
            mad[i] = np.median(np.abs(chunk - med)) + 1e-8
        return mad

    for ex in exs:
        inp = json.loads(ex["input"])
        out = json.loads(ex["output"])
        mad_series = rolling_mad(np.array(inp), window=5)
        preds = []
        for i in range(len(inp)):
            if i == 0:
                preds.append(inp[0])
                continue
            grad = abs(inp[i] - inp[i-1])
            norm_grad = grad / mad_series[i]
            w = int(np.clip(round(3 / (1.0 + norm_grad * scale_factor)), 1, 5))
            start = max(0, i - w + 1)
            preds.append(float(np.mean(inp[start:i+1])))
        mses.append(np.mean((np.array(out) - np.array(preds))**2))
    print(f"Scale factor {scale_factor} Mean MSE: {np.mean(mses):.4f}")
