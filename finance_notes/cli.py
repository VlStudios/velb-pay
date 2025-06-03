import argparse
from .storage import add_note, delete_note, list_notes


def main():
    parser = argparse.ArgumentParser(description="Simple financial notes manager")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a note")
    add_parser.add_argument("description", help="Note description")
    add_parser.add_argument("amount", type=float, help="Note amount")

    list_parser = subparsers.add_parser("list", help="List notes")

    del_parser = subparsers.add_parser("delete", help="Delete a note")
    del_parser.add_argument("id", type=int, help="Note id")

    args = parser.parse_args()

    if args.command == "add":
        note = add_note(args.description, args.amount)
        print(f"Added note {note.id}: {note.description} ({note.amount})")
    elif args.command == "list":
        notes = list_notes()
        for note in notes:
            print(f"{note.id}: {note.description} ({note.amount})")
    elif args.command == "delete":
        success = delete_note(args.id)
        if success:
            print(f"Deleted note {args.id}")
        else:
            print(f"Note {args.id} not found")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
