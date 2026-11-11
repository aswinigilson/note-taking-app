
import json
from pathlib import Path
from .note import Note


FILE_NAME = Path(__file__).resolve().parent.parent / "notes.json"


def save_notes(notes_list):
    try:
        data = [note.save() for note in notes_list]

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    except (OSError, TypeError) as error:
        print(f"Error saving notes: {error}")


def load_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Invalid notes data format")

        notes = []

        for item in data:

            note = Note(
                title=item["title"],
                content=item["content"],
                tags=item.get("tags", []),
                timestamp=item.get("timestamp")
            )

            notes.append(note)

        return notes

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: notes.json is corrupted. Starting with empty notes.")
        return []

    except (OSError, KeyError, TypeError, ValueError):
        print("Warning: Unable to load notes. Starting with empty notes.")
        return []
