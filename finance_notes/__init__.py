"""Simple financial notes package."""

from .storage import add_note, delete_note, list_notes, Note

__all__ = [
    "add_note",
    "delete_note",
    "list_notes",
    "Note",
]
