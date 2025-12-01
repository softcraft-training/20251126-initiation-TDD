import pytest

class LegacyGame:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        self.display(player_name + " was added")
        self.display("They are player number %s" % len(self.players))

        return True

    def display(self, s):
        print(s)

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        self.display("%s is the current player" % self.players[self.current_player])
        self.display("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                self.display("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                self.display(self.players[self.current_player] + \
                             '\'s new location is ' + \
                             str(self.places[self.current_player]))
                self.display("The category is %s" % self._current_category)
                self._ask_question()
            else:
                self.display("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            self.display(self.players[self.current_player] + \
                         '\'s new location is ' + \
                         str(self.places[self.current_player]))
            self.display("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': self.display(self.pop_questions.pop(0))
        if self._current_category == 'Science': self.display(self.science_questions.pop(0))
        if self._current_category == 'Sports': self.display(self.sports_questions.pop(0))
        if self._current_category == 'Rock': self.display(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                self.display('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                self.display(self.players[self.current_player] + \
                             ' now has ' + \
                             str(self.purses[self.current_player]) + \
                             ' Gold Coins.')
                self.in_penalty_box[self.current_player] = False
                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            self.display("Answer was correct!!!!")
            self.purses[self.current_player] += 1
            self.display(self.players[self.current_player] + \
                         ' now has ' + \
                         str(self.purses[self.current_player]) + \
                         ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        self.display('Question was incorrectly answered')
        self.display(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)

class Game:
    def __init__(self):
        self.players = Players()

        self.deck = QuestionDeck()

        self.can_try_to_get_out_of_penalty_box = False

    def is_playable(self):
        return self.players.number_of_players() >= 2

    def add(self, player_name):
        self.players.add_player(player_name)

        self.display(player_name + " was added")
        self.display("They are player number %s" % self.players.number_of_players())

        return True

    def roll(self, roll):
        current_player = self.players.current_player()

        self.display("%s is the current player" % current_player.name)
        self.display("They have rolled a %s" % roll)

        if current_player.in_penalty_box:
            if roll % 2 != 0:
                current_player.exit_penalty_box()
                self.display("%s is getting out of the penalty box" % current_player.name)
            else:
                self.display("%s is not getting out of the penalty box" % current_player.name)
                return

        current_player.move(roll)
        self._ask_question(current_player)

    def was_correctly_answered(self):
        current_player = self.players.current_player()

        if current_player.in_penalty_box:
            self.players.next_player()
            return True

        current_player.earn_coin()

        self.display("Answer was correct!!!!")
        self.display(current_player.name + ' now has ' + str(current_player.purse) + ' Gold Coins.')

        if current_player.did_win:
            self.players.next_player()
            return False

        self.players.next_player()
        return True

    def wrong_answer(self):
        current_player = self.players.current_player()

        if current_player.in_penalty_box:
            self.players.next_player()
            return True

        current_player.send_to_penalty_box()

        self.display('Question was incorrectly answered')
        self.display(current_player.name + " was sent to the penalty box")

        self.players.next_player()
        return True

    def _ask_question(self, player):
        question = self.deck.draw(player.place)

        self.display(player.name + '\'s new location is ' + str(player.place))
        self.display("The category is %s" % question.category)
        self.display(question.name)

    def _display(self, message):
        print(message)

class Question:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class QuestionDeck:
    def __init__(self):
        self.popQuestions = [Question("Pop Question " + str(x), "Pop") for x in range(50)]
        self.scienceQuestions = [Question("Science Question " + str(x), "Science") for x in range(50)]
        self.sportsQuestions = [Question("Sports Question " + str(x), "Sports") for x in range(50)]
        self.rockQuestions = [Question("Rock Question " + str(x), "Rock") for x in range(50)]

    def draw(self, place):
        if place == 0 or place == 4 or place == 8:
            return self.popQuestions.pop(0)

        if place == 1 or place == 5 or place == 9:
            return self.scienceQuestions.pop(0)

        if place == 2 or place == 6 or place == 10:
            return self.sportsQuestions.pop(0)

        return self.rockQuestions.pop(0)

class Player:
    def __init__(self, name):
        self.name = name
        self.place = 0
        self.purse = 0
        self.in_penalty_box = False

    def move(self, roll):
        self.place = self.place + roll
        if self.place > 11:
            self.place = self.place - 12

    def did_win(self):
        self.purse == 6

    def earn_coin(self):
        self.purse += 1

    def send_to_penalty_box(self):
        self.in_penalty_box = True

    def exit_penalty_box(self):
        self.in_penalty_box = False

class Players:
    def __init__(self):
        self.players = []
        self.current_player_index = 0

    def number_of_players(self):
        return len(self.players)

    def add_player(self, player_name):
        self.players.append(Player(player_name))

    def current_player(self):
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index += 1
        if self.current_player_index == len(self.players): self.current_player_index = 0

class TestableGame(Game):
    def __init__(self):
        super().__init__()
        self.output = []

    def display(self, message):
        self.output.append(message)

    def get_display(self):
        return self.output

class LegacyTestableGame(LegacyGame):
    def __init__(self):
        super().__init__()
        self.output = []

    def display(self, message):
        self.output.append(message)

    def get_display(self):
        return self.output

def runGameScenario(game):
    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    game.is_playable()

    for diceValue in range(20):
        game.roll(diceValue % 5 + 1)

        if diceValue % 9 == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

class TestTrivia:
    def test_golden_master(self):
        game = TestableGame()
        legacy = LegacyTestableGame()

        runGameScenario(game)
        runGameScenario(legacy)

        assert game.get_display() == legacy.get_display()
