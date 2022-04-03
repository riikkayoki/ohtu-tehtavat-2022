class TennisGame:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_score = 0
        self.player_2_score = 0
        self.score = ""
        self.score_dict = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __str__(self):
        return f"{self.score_dict[self.player_1_score]}-{self.score_dict[self.player_2_score]}"

    def update_score(self, player_name):
        if player_name == "player_1":
            self.player_1_score += 1
        else:
            self.player_2_score += 1

    def get_score(self):
        if self.player_1_score == self.player_2_score:
            self.score = self.check_for_tie()
        elif self.player_1_score >= 4 or self.player_2_score >= 4:
            self.score = self.check_for_win()
        else:
            self.score = self.__str__()
        return self.score

    def check_for_tie(self):
        if self.player_1_score <= 3:
            self.score = self.score_dict[self.player_1_score] + "-All"
        else:
            self.score = "Deuce"
        return self.score

    def check_for_win(self):
        score_difference = self.player_1_score - self.player_2_score

        if score_difference == 1:
            return "Advantage player 1"
        if score_difference == -1:
            return "Advantage player 2"
        if score_difference >= 2:
            return "Win for player 1"
        return "Win for player 2"