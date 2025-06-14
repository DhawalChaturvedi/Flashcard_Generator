import json
import os

def save_flashcards(flashcards, path="flashcards_db.json"):    #Function to save the content in the form of json file
    if os.path.exists(path):
        with open(path, 'r') as f:
            db = json.load(f)
    else:
        db = []
    db.extend(flashcards)
    with open(path, 'w') as f:
        json.dump(db, f, indent=2)

def load_flashcards(path="flashcards_db.json"):               #Function to load the content
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return []