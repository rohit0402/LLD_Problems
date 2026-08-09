from typing import List

class Book:
    def __init__(self,book_id:int,title:str,author:str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies :List = []

    def add_copy(self,copy) -> None:
        self.copies.append(copy)

    def get_available_copies(self) :
        for copy in self.copies:
            if copy.is_available():
                return copy

        return None