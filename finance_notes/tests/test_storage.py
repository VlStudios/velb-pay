import unittest
from pathlib import Path
import tempfile
from finance_notes.storage import add_note, list_notes, delete_note


class TestStorage(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.path = Path(self.tmpdir.name) / "test_notes.json"

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_add_and_list(self):
        add_note("first", 10.5, path=self.path)
        add_note("second", 20.0, path=self.path)
        notes = list_notes(path=self.path)
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[0].description, "first")
        self.assertAlmostEqual(notes[1].amount, 20.0)

    def test_delete(self):
        note = add_note("item", 5.0, path=self.path)
        deleted = delete_note(note.id, path=self.path)
        self.assertTrue(deleted)
        self.assertEqual(len(list_notes(path=self.path)), 0)
        deleted_again = delete_note(note.id, path=self.path)
        self.assertFalse(deleted_again)


if __name__ == "__main__":
    unittest.main()
