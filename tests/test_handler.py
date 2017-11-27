import unittest
import handler
import json
from tests.mock_alexa import MockAlexa

APPNAME = "greyhound advisor"

class TestHandler(unittest.TestCase):

    def setUp(self):
        self.alexa = MockAlexa(APPNAME, handler)
        self.alexa.hears("open {}".format(APPNAME))


    def test_launch(self):
        assert "Hello" in self.alexa.says()


    def test_timeout(self):
        self.alexa.timeout()
        assert "Thank you for speaking to me" in self.alexa.says()


    def test_help(self):
        self.alexa.hears("help")
        assert "Hello" in self.alexa.says()


    def test_stop(self):
        self.alexa.hears("stop")
        assert "Thank you for speaking to me" in self.alexa.says()


    def test_exit(self):
        self.alexa.hears("exit")
        assert "Thank you for speaking to me" in self.alexa.says()


    def test_eating_alcohol(self):
        self.alexa.hears("can a dog eat alcohol")
        assert "No, a dog must not eat alcohol" in self.alexa.says()


    def test_eating_beans(self):
        self.alexa.hears("can a dog eat beans")
        assert "I don't know about beans so cannot comment" in self.alexa.says()
