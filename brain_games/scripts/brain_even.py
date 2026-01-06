from brain_games.games.even_game import INSTRUCTION, game_even
from brain_games.scripts.engine import engine


def main():

    engine(game_even, INSTRUCTION)


if __name__ == "__main__":
    main()