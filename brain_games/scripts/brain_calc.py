from brain_games.games.calc_game import INSTRUCTION, game_calc
from brain_games.scripts.engine import engine


def main():

    engine(game_calc, INSTRUCTION)


if __name__ == "__main__":
    main()
