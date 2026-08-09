from typing import List
from enums.game_enums import Symbol

class Board:
    def __init__(self, size:int =3):
        self.size = size
        self.cells : List[List[Symbol]] = [[Symbol.EMPTY for _ in range(size)]for _ in range(size)]

    def is_valid_move(self,row:int,col:int)->bool:
        return (
            0<=row<self.size and 0<=col<self.size and self.cells[row][col]==Symbol.EMPTY
        )

    def make_move(self,row:int,col:int,symbol:Symbol)->None:
        if not self.is_valid_move(row,col):
            raise ValueError("Invalid move")

        self.cells[row][col] = symbol

    def check_winner(self,symbol:Symbol)->bool:
        for row in range(self.size):
            if all(self.cells[row][col]==symbol for col in range(self.size)):
                return True

        for col in range(self.size):
            if all(self.cells[row][col]==symbol for row in range(self.size)):
                return True

        if all(self.cells[i][i]==symbol for i in range(self.size)):
            return True

        if all(self.cells[i][self.size -1 -i]==symbol for i in range(self.size)):
            return True

        return False

    def is_full(self)->bool:
        return all(self.cells[row][col]!=Symbol.EMPTY for row in range(self.size) for col in range(self.size))

    def display(self)->None:
        for row in range(self.size):
            print("|".join(self.cells[row][col].value for col in range(self.size)))

            if row<self.size-1:
                print("-"*(self.size*4-3))