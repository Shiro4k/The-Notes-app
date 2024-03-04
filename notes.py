import json
import os
import datetime

notes_file = "notes.json"


def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as file:
            notes = json.load(file)
        return notes
    else:
        return {}


def save_notes(notes):
    with open(notes_file, 'w') as file:
        json.dump(notes, file, indent=4)


def add_note():
    notes = load_notes()
    note_id = input("Enter note id: ")
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes[note_id] = {
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    save_notes(notes)
    print("Note added successfully.")


def read_note():
    notes = load_notes()
    note_id = input("Enter note id to read: ")

    if note_id in notes:
        note = notes[note_id]
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Timestamp: {note['timestamp']}")
    else:
        print("Note not found.")


def edit_note():
    notes = load_notes()
    note_id = input("Enter note id to edit: ")

    if note_id in notes:
        title = input("Enter new title: ")
        body = input("Enter new body: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        notes[note_id]['title'] = title
        notes[note_id]['body'] = body
        notes[note_id]['timestamp'] = timestamp

        save_notes(notes)
        print("Note edited successfully.")
    else:
        print("Note not found.")


def get_all_notes():
    notes = load_notes()
    result = []
    for note in notes:
        result.append({"id": note, "title": notes[note]['title'], "timestamp": notes[note]['timestamp']})
    return result


def delete_note():
    notes = load_notes()
    note_id = input("Enter note id to delete: ")

    if note_id in notes:
        del notes[note_id]
        save_notes(notes)
        print("Note deleted successfully.")
    else:
        print("Note not found.")


def main_menu():
    while True:
        print("\n1. Add Note")
        print("2. Read Note")
        print("3. Read All Notes")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            read_note()
        elif choice == '3':
            print(get_all_notes())
        elif choice == '4':
            edit_note()
        elif choice == '5':
            delete_note()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()