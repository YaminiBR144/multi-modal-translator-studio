import json

def save_history(data, filename="history.json"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")

def load_history(filename="history.json"):
    history = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                history.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass
    return history
