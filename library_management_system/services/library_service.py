from entities.book import Book
from entities.member import Member
from entities.loan import Loan

class Library:
    def __init__(self,fine_calculator):
        self.books={}
        self.mebers={}
        self.loans={}

        self.fine_calculator=fine_calculator

    def add_book(self,book:Book)->None:
        self.books[book.book_id]=book

    def add_member(self,member:Member)->None:
        self.mebers[member.member_id]=member

    def search_book(self,title:str):
        result=[]
        for book in self.books.values():
            if title.lower() in book.title.lower():
                result.append(book)

        return result

    def borrow_book(self,member_id:str,book_id:str,loan_id:str)->Loan:
        if member_id not in self.mebers:
            raise Exception("Member not found.")

        if book_id not in self.books:
            raise Exception("Book not found.")

        member=self.mebers[member_id]
        book=self.books[book_id]
        copy=book.get_available_copies()

        if copy is None:
            raise Exception("No available copies.")

        copy.borrow()
        loan=Loan(loan_id,member,copy)
        self.loans[loan_id]=loan
        return loan

    def return_book(self,loan_id:str)->float:
        if loan_id not in self.loans:
            raise Exception("Loan not found.")

        loan=self.loans[loan_id]
        if loan.return_date is not None:
            raise Exception("Loan is already closed.")

        loan.close()

        loan.book_copy.return_book()

        fine=self.fine_calculator.calculate(loan.due_date,loan.return_date)
        return fine
