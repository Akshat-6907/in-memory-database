import json

def save(store, filename):
    with open(filename, "w") as f:
        json.dump(store, f)

def load(store, filename):
    try:
        with open(filename, "r") as f:
            store.clear()
            store.update(json.load(f))
            print("Loaded from database")
    except FileNotFoundError:
        print("ERROR: file not found")