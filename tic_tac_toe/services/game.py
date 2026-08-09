from entities.player import Player
from entities.board import Board

class Game:
    def __init__(self,player1:Player, player2:Player,board_size:int=3):
        self.board = Board(board_size)
        self.players = [player1,player2]
        self.current_player_index =0
        self.game_over = False
        self.winner = None

    @property
    def current_player(self)->Player:
        return self.players[self.current_player_index]

    def switch_player(self)->None:
        self.current_player_index =1 - self.current_player_index

    def make_move(self,row:int,col:int)->None:
        if self.game_over:
            raise ValueError("Game is over")

        player = self.current_player

        self.board.make_move(row,col,player.symbol)
        if self.board.check_winner(player.symbol):
            self.winner = player
            self.game_over = True
            return
        
        if self.board.is_full():
            self.game_over = True
            return

        self.switch_player()

    def display(self)->None:
        self.board.display()