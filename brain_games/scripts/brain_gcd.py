from brain_games.games.gcd_game import INSTRUCTION, game_gcd
from brain_games.scripts.engine import engine


def main():

    engine(game_gcd, INSTRUCTION)


if __name__ == "__main__":
    main()