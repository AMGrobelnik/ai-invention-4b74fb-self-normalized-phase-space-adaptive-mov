import os
import json
import numpy as np

def generate_ou_process(n=100, theta=0.1, mu=0.0, sigma=0.5, seed=42):
    np.random.seed(seed)
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = x[t-1] + theta * (mu - x[t-1]) + sigma * np.random.randn()
    return x

def compute_adaptive_ma(series, min_w=1, max_w=5):
    preds = []
    n = len(series)
    for t in range(2, n):
        grad = abs(series[t-1] - series[t-2])
        window = max_w - int(np.clip(grad * 2, 0, max_w - min_w))
        window = max(min_w, min(window, t))
        start = max(0, t - window)
        preds.append(np.mean(series[start:t]))
    return np.array(preds)

def compute_static_ma(series, window=3):
    preds = []
    n = len(series)
    for t in range(2, n):
        start = max(0, t - window)
        preds.append(np.mean(series[start:t]))
    return np.array(preds)

def compute_naive(series):
    preds = []
    n = len(series)
    for t in range(2, n):
        preds.append(series[t-1])
    return np.array(preds)

def main():
    os.makedirs('/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results', exist_ok=True)
    
    n_trials = 60
    n_steps = 100
    
    examples = []
    for i in range(n_trials):
        series = generate_ou_process(n=n_steps, seed=i)
        actuals = series[2:]
        
        pred_adap = compute_adaptive_ma(series)
        pred_stat = compute_static_ma(series, window=3)
        pred_naiv = compute_naive(series)
        
        for t_idx in range(len(actuals)):
            ex = {
                "input": f"Series trial {i}, step {t_idx+2}",
                "output": str(float(actuals[t_idx])),
                "metadata_trial": i,
                "metadata_step": t_idx + 2,
                "predict_adaptive_ma": str(float(pred_adap[t_idx])),
                "predict_static_ma": str(float(pred_stat[t_idx])),
                "predict_naive": str(float(pred_naiv[t_idx]))
            }
            examples.append(ex)
            
    dataset_obj = {
        "datasets": [
            {
                "dataset": "ornstein_uhlenbeck_synthetic",
                "examples": examples
            }
        ]
    }
    
    for fname in ['method_out.json', 'full_method_out.json', 'mini_method_out.json', 'preview_method_out.json', 'results/results.json']:
        out_path = os.path.join('/ai-inventor/aii_data/runs/run_KZZ3JEauA8v3/3_invention_loop/iter_1/gen_art/gen_art_experiment_1', fname)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w') as f:
            json.dump(dataset_obj, f, indent=2)
            
    print("Regenerated all JSON outputs with datasets schema.")

if __name__ == '__main__':
    main()
