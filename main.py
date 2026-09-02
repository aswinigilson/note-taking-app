from note_manager import Note, save_notes, load_notes


def display_menu():
    print("\n" + "=" * 40)
    print("          NOTE-TAKING APP")
    print("=" * 40)
    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Filter by Tag")
    print("6. Exit")
    print("=" * 40)


def add_note(notes):
    print("\n--- Add Note ---")

    title = input("Enter title: ").strip()
    content = input("Enter content: ").strip()

    tag_input = input("Enter tags (comma-separated): ").strip()

    if tag_input:
        tags = [tag.strip() for tag in tag_input.split(",")]
    else:
        tags = []

    note = Note(title, content, tags)
    notes.append(note)

    save_notes(notes)

    print("\nNote added successfully!")


def view_notes(notes):
    print("\n--- All Notes ---")

    if not notes:
        print("No notes available.")
        return

    for index, note in enumerate(notes, start=1):
        print(f"\nNote #{index}")
        note.display()


def search_notes(notes):
    print("\n--- Search Notes ---")

    term = input("Enter search keyword: ").strip()

    found = False

    for index, note in enumerate(notes, start=1):
        if note.matches_search(term):
            print(f"\nNote #{index}")
            note.display()
            found = True

    if not found:
        print("No matching notes found.")


def delete_note(notes):
    print("\n--- Delete Note ---")

    if not notes:
        print("No notes available.")
        return

    view_notes(notes)

    try:
        number = int(input("Enter note number to delete: "))

        if 1 <= number <= len(notes):
            deleted_note = notes.pop(number - 1)

            save_notes(notes)

            print(f"Deleted note: {deleted_note.title}")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


def filter_by_tag(notes):
    print("\n--- Filter by Tag ---")

    tag = input("Enter tag: ").strip().lower()

    found = False

    for index, note in enumerate(notes, start=1):
        if any(note_tag.lower() == tag for note_tag in note.tags):
            print(f"\nNote #{index}")
            note.display()
            found = True

    if not found:
        print(f"No notes found with tag '{tag}'.")


def main():
    notes = load_notes()

    print("Notes loaded successfully.")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            delete_note(notes)

        elif choice == "5":
            filter_by_tag(notes)

        elif choice == "6":
            save_notes(notes)
            print("\nNotes saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()