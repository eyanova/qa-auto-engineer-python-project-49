from brain_games.games.prime_game import INSTRUCTION, game_prime
from brain_games.scripts.engine import engine


def main():

    engine(game_prime, INSTRUCTION)


if __name__ == "__main__":
    main()