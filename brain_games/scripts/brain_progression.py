from brain_games.games.progression_game import INSTRUCTION, game_progression
from brain_games.scripts.engine import engine


def main():

    engine(game_progression, INSTRUCTION)


if __name__ == "__main__":
    main()