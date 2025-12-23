import json
import os
from datetime import datetime

HISTORY_DIR = "history"

def save_scan(username, target, result):
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)

    user_file = os.path.join(HISTORY_DIR, f"{username}.json")

    entry = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "target": target,
        "result": result
    }

    data = []
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(user_file, "w") as f:
        json.dump(data, f, indent=4)

def load_history(username):
    user_file = os.path.join(HISTORY_DIR, f"{username}.json")
    if not os.path.exists(user_file):
        return []
    with open(user_file, "r") as f:
        return json.load(f)
