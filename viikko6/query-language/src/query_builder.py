
from matchers import And, HasAtLeast, PlaysIn, Or, HasFewerThan, All

class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def build(self):
        return self._query

    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))

    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))