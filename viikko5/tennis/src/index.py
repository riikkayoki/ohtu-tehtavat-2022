from tennis_game import TennisGame


def main():
    game = TennisGame("player_1", "player_2")

    print(game.get_score())

    game.update_score("player_1")
    print(game.get_score())

    game.update_score("player_1")
    print(game.get_score())

    game.update_score("player_2")
    print(game.get_score())

    game.update_score("player_1")
    print(game.get_score())

    game.update_score("player_1")
    print(game.get_score())


if __name__ == "__main__":
    main()
