class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def __str__(self):
        return f'{self.name:20} {self.team:5} {self.goals:1} + {self.assists:1} = {self.__eq__()}'

    def __eq__(self):
        return self.goals + self.assists

