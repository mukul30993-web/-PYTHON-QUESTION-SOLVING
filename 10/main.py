# ======================================
# Library Management System
# Author: Mukul
# ======================================

books = []


# ---------- Book Functions ----------

def add_book():
    """Add a new book."""
    pass


def display_books():
    """Display all books."""
    pass


def search_book():
    """Search a book."""
    pass


def issue_book():
    """Issue a book."""
    pass


def return_book():
    """Return a book."""
    pass


def delete_book():
    """Delete a book."""
    pass


def update_book():
    """Update book details."""
    pass


def total_books():
    """Show library statistics."""
    pass


def save_data():
    """Save books to JSON file."""
    pass


def load_data():
    """Load books from JSON file."""
    pass


# ---------- Menu ----------

def menu():
    print("\n" + "=" * 40)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Update Book")
    print("8. Total Books")
    print("9. Save Data")
    print("10. Load Data")
    print("11. Exit")
    print("=" * 40)


# ---------- Main Program ----------

def main():

    while True:

        menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            update_book()

        elif choice == "8":
            total_books()

        elif choice == "9":
            save_data()

        elif choice == "10":
            load_data()

        elif choice == "11":
            print("\nThank you for using the Library Management System.")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()