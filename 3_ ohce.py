import unittest.mock
from datetime import datetime
import pytest

class ConsoleIO:
    def readLine(self):
        return input("$")

    def writeLine(self, message):
        print("> " + message)
        pass

class Oche:
    def __init__(self, io, dt):
        self.io = io
        self.firstname = io.readLine()

        if dt.hour >= 6 and dt.hour < 12:
            io.writeLine("Buenos dias " + self.firstname)
        elif dt.hour >= 12 and dt.hour < 20:
            io.writeLine("Buenas tardes " + self.firstname)
        else:
            io.writeLine("Buenas noches "+ self.firstname)

    def listen(self):
        shouldExit = False

        while not shouldExit:
            entry = self.io.readLine()
            if entry == "Stop!":
                self.io.writeLine("Adios " + self.firstname)

                shouldExit = True
            else:
                output = entry[::-1]
                self.io.writeLine(output)
                if output == entry:
                    self.io.writeLine("Bonita palabra")

class TestOche:
    def test_should_greet_person_with_buenos_dias(self, mocker):
        io = mocker.Mock()
        io.readLine.return_value = "Mickael"
        io.writeLine.return_value = None

        Oche(io, datetime(2026, 1, 1, 10, 30))

        io.writeLine.assert_called_with("Buenos dias Mickael")

    def test_should_greet_person_with_buenas_tardes(self, mocker):
        io = mocker.Mock()
        io.readLine.return_value = "Mickael"
        io.writeLine.return_value = None

        Oche(io, datetime(2026, 1, 1, 15, 30))

        io.writeLine.assert_called_with("Buenas tardes Mickael")

    def test_should_greet_person_with_buenas_noches(self, mocker):
        io = mocker.Mock()
        io.readLine.return_value = "Mickael"
        io.writeLine.return_value = None

        Oche(io, datetime(2026, 1, 1, 21, 30))

        io.writeLine.assert_called_with("Buenas noches Mickael")


    def test_should_return_reverse_entry(self, mocker):
        io = mocker.Mock()
        io.readLine.side_effect = [ "mickael", "face", "Stop!" ]
        io.writeLine.return_value = None

        oche = Oche(io, datetime(2026, 1, 1, 21, 30))

        oche.listen()

        assert io.writeLine.mock_calls == [
            unittest.mock.call("Buenas noches mickael"),
            unittest.mock.call("ecaf"),
            unittest.mock.call("Adios mickael"),
        ]

    def test_should_exit(self, mocker):
        io = mocker.Mock()
        io.readLine.side_effect = [ "mickael", "Stop!"]
        io.writeLine.return_value = None

        oche = Oche(io, datetime(2026, 1, 1, 21, 30))

        oche.listen()
        assert io.writeLine.mock_calls == [
            unittest.mock.call("Buenas noches mickael"),
            unittest.mock.call("Adios mickael"),
        ]

    def test_should_return_bonita_palabra_when_palindrome(self, mocker):
        io = mocker.Mock()
        io.readLine.side_effect = [ "mickael", "ata", "Stop!" ]
        io.writeLine.return_value = None

        oche = Oche(io, datetime(2026, 1, 1, 21, 30))

        oche.listen()

        assert io.writeLine.mock_calls[1] == unittest.mock.call("ata")
        assert io.writeLine.mock_calls[2] == unittest.mock.call("Bonita palabra")
