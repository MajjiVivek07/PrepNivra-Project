import json, os
FILE = "prepnivra_data.json"
def load_data():
    if not os.path.exists(FILE): return {"profile": {}, "scores": [], "coding": []}
    try:
        with open(FILE, "r", encoding="utf-8") as f: data = json.load(f)
        data.setdefault("profile", {}); data.setdefault("scores", []); data.setdefault("coding", [])
        return data
    except (OSError, json.JSONDecodeError):
        print("Could not read saved data; starting fresh.")
        return {"profile": {}, "scores": [], "coding": []}
def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f: json.dump(data, f, indent=4)
