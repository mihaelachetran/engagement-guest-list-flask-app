
import json
import os


FILE_NAME = "guests.json"


def load_guests():
    if not os.path.exists(FILE_NAME):
        return[]
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return[]
  


def save_guests(guests):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(guests, file, indent=4, ensure_ascii=False)

