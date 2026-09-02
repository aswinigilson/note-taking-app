import json
from .note import Note


FILE_NAME = "notes.json"


def save_notes(notes_list):
    try:
        data = [note.save() for note in notes_list]

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except OSError as error:
        print(f"Error saving notes: {error}")


def load_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        notes = []

        for item in data:
            note = Note(
                item["title"],
                item["content"],
                item["tags"],
                item["timestamp"]
            )
            notes.append(note)

        return notes

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: notes.json is corrupted. Starting with empty notes.")
        return []

    except (OSError, KeyError, TypeError):
        print("Warning: Unable to load notes. Starting with empty notes.")
        return []