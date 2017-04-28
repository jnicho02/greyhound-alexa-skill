import unittest
import handler


class TestHandler(unittest.TestCase):

    def test_session_started(self):
        service_request = {
          "session": {
            "sessionId": "SessionId.c1bbb5bf-29dd-430b-8476-50fd4958200c",
            "application": {
              "applicationId": "amzn1.ask.skill.5858d1a6-2fce-4ae7-889a-d2932738db27"
            },
            "attributes": {},
            "user": {
              "userId": "amzn1.ask.account.AEUPDEZTCS5ZATUSUS6ZNPBZ7FJ66NRFEWPWOR7LB2HHT3EPN42RTYUXNLBF62TXPVKTYWXCLZXIOI3AHNOPM4AAANBFOXRSD2PSTGBYPQ7WLJDRRHGX3LNQY5OJRO3LQRWORZNSJOPQSJKADPCBCBSVSQ2YAQRTJY2SINVK3TGCPKMRBCYHHCN7BXKTJDXS45FTXU3E74M25EI"
            },
            "new": 'false'
          },
          "request": {
            "type": "IntentRequest",
            "requestId": "EdwRequestId.2de16d67-ca96-4417-b307-add19c9fe10d",
            "locale": "en-GB",
            "timestamp": "2017-04-28T09:29:15Z",
            "intent": {
              "name": "CanItEat",
              "slots": {
                "food": {
                  "name": "food",
                  "value": "chocolate"
                }
              }
            }
          },
          "version": "1.0"
        }
        response = handler.hello(service_request, None)
#        self.assertEqual("dg", response)


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
        self.assertEqual("No, a greyhound must not eat alcohol. Ingestion can lead to injury, disorientation, sickness, urination problems or even coma or death from alcohol poisoning", response)


    def test_can_it_eat_apple(self):
        intent = {
            "name": "CanItEat",
            "slots": {
                "food": {
                  "name": "food",
                  "value": "apple"
                }
            }
        }
        response = handler.can_it_eat(intent)
        self.assertEqual("A greyhound should not eat apple. The seeds contain cyanogenic glycosides which can result in cyanide poisoning.", response)


    def test_can_it_eat_kibbles(self):
        intent = {
            "name": "CanItEat",
            "slots": {
                "food": {
                  "name": "food",
                  "value": "kibbles"
                }
            }
        }
        response = handler.can_it_eat(intent)
        self.assertEqual("Yes, a greyhound can eat kibbles.", response)
