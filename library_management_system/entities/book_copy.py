from enums.library_enums import BookStatus

class BookCopy:
    def __init__(self,copy_id:str):
        self.copy_id = copy_id
        self.status = BookStatus.AVAILABLE

    def is_available(self) -> bool:
        return self.status == BookStatus.AVAILABLE

    def borrow(self) -> None:
        if not self.is_available():
            raise Exception("Book copy is not available for borrowing.")
        self.status = BookStatus.BORROWED

    def return_book(self)->None:
        if self.is_available():
            raise Exception("Book copy is not borrowed.")
        self.status = BookStatus.AVAILABLE