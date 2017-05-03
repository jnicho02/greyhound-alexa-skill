import unittest
import handler
from tests.mock_alexa import MockAlexa

class TestHandler(unittest.TestCase):


    def test_launch(self):
        alexa = MockAlexa("greyhound advisor", handler)
        service_response = alexa.ask("open greyhound advisor")
        assert "Hello" in service_response["response"]["outputSpeech"]["text"]


    def test_timeout(self):
        alexa = MockAlexa("greyhound advisor", handler)
        service_response = alexa.ask("open greyhound advisor")
        service_response = alexa.timeout()
        assert "Thank you for speaking to me" in service_response["response"]["outputSpeech"]["text"]


    def test_help(self):
        alexa = MockAlexa("greyhound advisor", handler)
        alexa.ask("open greyhound advisor")
        service_response = alexa.ask("help")
        assert "Hello" in service_response["response"]["outputSpeech"]["text"]


    def test_exit(self):
        alexa = MockAlexa("greyhound advisor", handler)
        alexa.ask("open greyhound advisor")
        service_response = alexa.ask("exit")
        assert "Thank you for speaking to me" in service_response["response"]["outputSpeech"]["text"]


    def test_can_it_eat_alcohol_unit(self):
        intent = {
            "name": "CanItEat",
            "slots": {
                "food": {
                  "name": "food",
                  "value": "alcohol"
                }
            }
        }
        response = handler.can_it_eat(intent)
        assert "No, a greyhound must not eat alcohol" in response


    def test_can_it_eat_monkeys_unit(self):
        intent = {
            "name": "CanItEat",
            "slots": {
                "food": {
                  "name": "food",
                  "value": "monkeys"
                }
            }
        }
        response = handler.can_it_eat(intent)
        assert "I am not sure" in response


    def test_can_it_eat_alcohol(self):
        alexa = MockAlexa("greyhound advisor", handler)
        alexa.ask("open greyhound advisor")
        service_response = alexa.ask("can a greyhound eat alcohol")
        assert "No, a greyhound must not eat alcohol" in service_response["response"]["outputSpeech"]["text"]
