import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List


@dataclass
class Note:
    id: int
    description: str
    amount: float


import os
DEFAULT_PATH = Path(os.environ.get("NOTES_PATH", "notes.json"))


def load_notes(path: Path = DEFAULT_PATH) -> List[Note]:
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return [Note(**item) for item in data]
    return []


def save_notes(notes: List[Note], path: Path = DEFAULT_PATH) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([asdict(n) for n in notes], f, indent=2)


def add_note(description: str, amount: float, path: Path = DEFAULT_PATH) -> Note:
    notes = load_notes(path)
    note_id = max((n.id for n in notes), default=0) + 1
    note = Note(id=note_id, description=description, amount=amount)
    notes.append(note)
    save_notes(notes, path)
    return note


def delete_note(note_id: int, path: Path = DEFAULT_PATH) -> bool:
    notes = load_notes(path)
    new_notes = [n for n in notes if n.id != note_id]
    if len(new_notes) == len(notes):
        return False
    save_notes(new_notes, path)
    return True


def list_notes(path: Path = DEFAULT_PATH) -> List[Note]:
    return load_notes(path)
