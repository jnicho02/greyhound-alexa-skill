import unittest
import handler


class TestHandler(unittest.TestCase):


    def test_can_it_eat_alcohol(self):
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
        assert "No, a dog must not eat alcohol" in response


    def test_can_it_eat_monkeys(self):
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
        assert "I don't know" in response


    def test_alexa_stop(self):
        intent = {
            "name": "CanItEat",
            "confirmationStatus": "NONE",
            "slots": {
                "food": {
                  "name": "food",
                  "confirmationStatus": "NONE"
                }
            }
        }
        response = handler.can_it_eat(intent)
        assert "I don't know" in response
