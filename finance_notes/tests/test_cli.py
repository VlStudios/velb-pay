import unittest
import subprocess
import sys
from pathlib import Path
import tempfile
import json


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.notes_path = Path(self.tmpdir.name) / "notes.json"
        self.env = {"PYTHONPATH": str(Path(__file__).resolve().parents[1])}

    def tearDown(self):
        self.tmpdir.cleanup()

    def run_cli(self, *args):
        cmd = [sys.executable, "-m", "finance_notes.cli", *args]
        return subprocess.run(
            cmd,
            env={**self.env, "NOTES_PATH": str(self.notes_path)},
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )

    def test_add_list_delete(self):
        r1 = self.run_cli("add", "Item", "3")
        self.assertIn("Added note", r1.stdout)
        r2 = self.run_cli("list")
        self.assertIn("Item", r2.stdout)
        note_id = json.loads(self.notes_path.read_text())[0]["id"]
        r3 = self.run_cli("delete", str(note_id))
        self.assertIn("Deleted note", r3.stdout)


if __name__ == "__main__":
    unittest.main()
