import unittest

from tennis_game import TennisGame

test_cases = [
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Forty-All"),
    (4, 4, "Deuce"),

    (1, 0, "Fifteen-Love"),
    (0, 1, "Love-Fifteen"),
    (2, 0, "Thirty-Love"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for player 1"),
    (0, 4, "Win for player 2"),

    (2, 1, "Thirty-Fifteen"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for player 1"),
    (1, 4, "Win for player 2"),

    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for player 1"),
    (2, 4, "Win for player 2"),

    (4, 3, "Advantage player 1"),
    (3, 4, "Advantage player 2"),
    (5, 4, "Advantage player 1"),
    (4, 5, "Advantage player 2"),
    (15, 14, "Advantage player 1"),
    (14, 15, "Advantage player 2"),

    (6, 4, "Win for player 1"),
    (4, 6, "Win for player 2"),
    (16, 14, "Win for player 1"),
    (14, 16, "Win for player 2"),
]


def play_game(player_1_score, player_2_score):
    game = TennisGame("player_1", "player_2")
    for score in range(max(player_1_score, player_2_score)):
        if score < player_1_score:
            game.update_score("player_1")
        if score < player_2_score:
            game.update_score("player_2")
    return game


class TestTennis(unittest.TestCase):
    def test_score(self):
        for test_case in test_cases:
            (player_1_score, player_2_score, score) = test_case
            game = play_game(player_1_score, player_2_score)
            self.assertEqual(score, game.get_score())
