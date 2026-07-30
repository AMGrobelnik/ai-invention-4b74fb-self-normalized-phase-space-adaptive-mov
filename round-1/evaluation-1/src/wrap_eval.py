import json

def main():
    with open("eval_out.json", "r") as f:
        data = json.load(f)
    
    wrapped = {
        "datasets": [
            {
                "dataset": "evaluation_results",
                "examples": [data]
            }
        ]
    }
    
    with open("eval_out_wrapped.json", "w") as f:
        json.dump(wrapped, f, indent=2)

if __name__ == "__main__":
    main()
