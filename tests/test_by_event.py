import unittest
import handler
import json
from tests.mock_alexa import MockAlexa

APPNAME = "greyhound advisor"

class TestByEvent(unittest.TestCase):


    def test_launch(self):
        with open('tests/fixtures/launch.json') as json_data:
            event = json.load(json_data)
        response = handler.hello(event, None)
        assert "Hello" in response['response']["outputSpeech"]["text"]


    def test_apples(self):
        with open('tests/fixtures/can_a_dog_eat_apples.json') as json_data:
            event = json.load(json_data)
        response = handler.hello(event, None)
        assert "I don't know about apples so cannot comment" in response['response']["outputSpeech"]["text"]


    def test_marshmallows(self):
        with open('tests/fixtures/can_a_dog_eat_marshmallows.json') as json_data:
            event = json.load(json_data)
        response = handler.hello(event, None)
        assert "I don't know about marshmallows so cannot comment" in response['response']["outputSpeech"]["text"]


    def test_stop(self):
        with open('tests/fixtures/stop.json') as json_data:
            event = json.load(json_data)
        response = handler.hello(event, None)
        assert "Thank you for speaking to me." in response['response']["outputSpeech"]["text"]
