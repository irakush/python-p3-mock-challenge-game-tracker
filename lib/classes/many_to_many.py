class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        # else:
        #     raise Exception(
        #         "Titles must be of type str / Titles must be longer than 0 characters / Should not be able to change after the game is instantiated"
        #     )

    def results(self, new_result=None):
        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def players(self, new_player=None):
        if (
            new_player
            and isinstance(new_player, Player)
            and new_player not in self._players
        ):
            self._players.append(new_player)
        return self._players

    def average_score(self, player):
        player_scores = [
            each_r.score for each_r in self._results if each_r.player == player
        ]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        # else:
        #     raise Exception(
        #         "Usernames must be of type str / Usernames must be between 2 and 16 characters, inclusive."
        #     )

    def results(self, new_result=None):
        if new_result and isinstance(new_result, Result):
            if new_result not in self._results:
                self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        # return unique list of the games
        return list(set(self._games_played))  # self._games_played

    def played_game(self, game):
        return game in self._games_played  # true or false

    def num_times_played(self, game):
        return len([re for re in self._results if re.game == game])


class Result:
    all = []

    def __init__(self, player, game, score):
        # for result in Result.all:
        #     if result._player == player and result._game == game:
        #         return

        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

        player.results(self)

        player.games_played(game)

        game.results(self)
        game.players(player)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score
        # else:
        #     raise Exception(
        #         "Scores must be of type int / Scores must be between 1 and 5000, inclusive / Should not be able to change after the result is instantiated"
        #     )

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        # from classes.player import Player

        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Must be an instance of Player class")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Must be an instance of Game class")
