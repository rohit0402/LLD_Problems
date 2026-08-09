from entities.book import Book
from entities.book_copy import BookCopy
from entities.member import Member
from services.fine_calculator import FineCalculator
from services.library_service import Library


def main():
    fine_calculator = FineCalculator(rate_per_day=10.0)
    library = Library(fine_calculator)

    print("========================================")
    print("   WELCOME TO LIBRARY MANAGEMENT SYSTEM ")
    print("========================================")

    while True:
        print("\n---------------- MENU ----------------")
        print("1. Add Book & Copies")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        print("--------------------------------------")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            try:
                book_id = input("Enter Book ID (e.g., B001): ").strip()
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                num_copies = int(
                    input("Enter number of copies to add: ").strip()
                )

                book = Book(book_id=book_id, title=title, author=author)
                for i in range(1, num_copies + 1):
                    copy_id = f"C{book_id}_{i}"
                    book.add_copy(BookCopy(copy_id))

                library.add_book(book)
                print(
                    f"\n[Success] Added '{title}' with {num_copies} copies."
                )
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice == "2":
            try:
                member_id = input("Enter Member ID (e.g., M001): ").strip()
                name = input("Enter Member Name: ").strip()

                member = Member(member_id, name)
                library.add_member(member)
                print(f"\n[Success] Registered member '{name}'.")
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice == "3":
            try:
                member_id = input("Enter Member ID: ").strip()
                book_id = input("Enter Book ID: ").strip()
                loan_id = input("Enter Loan ID (e.g., L001): ").strip()

                loan = library.borrow_book(
                    member_id=member_id, book_id=book_id, loan_id=loan_id
                )
                print(
                    f"\n[Success] Borrowed copy '{loan.book_copy.copy_id}' under Loan ID '{loan_id}'."
                )
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice == "4":
            try:
                loan_id = input("Enter Loan ID: ").strip()

                fine = library.return_book(loan_id=loan_id)
                print(
                    f"\n[Success] Book returned successfully. Total Fine: ₹{fine}"
                )
            except Exception as e:
                print(f"\n[Error]: {e}")

        elif choice == "5":
            print("\nExiting system. Goodbye!")
            break

        else:
            print("\n[Invalid Option]: Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()