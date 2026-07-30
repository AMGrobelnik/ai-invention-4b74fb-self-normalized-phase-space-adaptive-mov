import json
import numpy as np

# Load a dataset and test 3-point moving average vs naive last-value forecast
path = "/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets/ou_process_low_noise.json"
with open(path, "r") as f:
    data = json.load(f)["values"]

series = np.array(data[:100]) # short series

# Naive forecast: y_hat[t] = y[t-1]
# 3-point moving average forecast: y_hat[t] = mean(y[t-3:t])

y_true = series[3:]
naive_pred = series[2:-1]

ma3_pred = []
for i in range(3, len(series)):
    ma3_pred.append(np.mean(series[i-3:i]))
ma3_pred = np.array(ma3_pred)

naive_mse = np.mean((y_true - naive_pred) ** 2)
ma3_mse = np.mean((y_true - ma3_pred) ** 2)

print(f"Naive MSE: {naive_mse:.4f}")
print(f"3-point MA MSE: {ma3_mse:.4f}")
print(f"3-point MA beats naive: {ma3_mse < naive_mse}")
