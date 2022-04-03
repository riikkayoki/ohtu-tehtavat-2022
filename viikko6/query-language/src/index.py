from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, Or, HasFewerThan

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
    #Not(HasAtLeast(1, "goals")),
    #)

    matcher = Or(
    HasAtLeast(30, "goals"),
    HasAtLeast(50, "assists")
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
