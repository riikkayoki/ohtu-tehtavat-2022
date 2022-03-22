class PlayerStats:
    def __init__(self, playerReader):
        self.players = playerReader.get_players()
        self.players.sort(key = lambda x: x.__eq__(), reverse = True)

    def top_scorers_by_nationality(self, country):
        country_players = []

        for player in self.players:
            if player.nationality == country:
                country_players.append(player)
        return country_players
