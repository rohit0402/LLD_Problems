from entities.player import Player
from services.game import Game
from enums.game_enums import Symbol

player1 = Player("Player 1", Symbol.X)
player2 = Player("Player 2", Symbol.O)

game = Game(player1,player2)

while not game.game_over:
    game.display()
    ("="*20).center(20)
    try:
        row = int(input(f"{game.current_player.name}, enter row: "))
        col = int(input(f"{game.current_player.name}, enter col: "))
        game.make_move(row,col)
    except ValueError:
        print("Invalid input. Please enter integers for row and column.")
        continue

game.display()

if game.winner is not None:
    print(f"{game.winner.name} wins!")
else:
    print("It's a draw!")