from __future__ import print_function
import json

def hello_world(event, context):
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Go Serverless v1.0! Your function executed successfully!',
            }
        }
    }
    return response


def hello(event, context):
    """ handle Amazon Alexa events.

    routes the common Alexa request types to event methods.
    """

    if event['session']['new']:
        on_session_started(event['request'], event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        intent_name = event['request']['intent']['name']
        if intent_name == "AMAZON.HelpIntent":
            return on_help(event['request'], event['session'])
        elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
            return on_session_ended(event['request'], event['session'])
        else:
            return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

# --------------- Events ------------------

def on_session_started(request, session):
    print("on_session_started requestId=" + request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(request, session):
    return welcome()


def on_help(request, session):
    return welcome()


def on_session_ended(request, session):
    print("on_session_ended requestId=" + request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


def on_intent(request, session):
    intent = request['intent']
    intent_name = intent['name']

#        raise ValueError("Invalid intent")

    things_a_greyhound_can_eat = ['kibbles']
    things_a_greyhound_cannot_eat = ['chocolate']

    session_attributes = {}
    card_title = intent_name

    food = value(intent, 'food')
    say = "I am not sure about {}".format(food)

    if food in things_a_greyhound_cannot_eat:
        say = "No, a greyhound cannot eat {}.".format(food)
    elif food in things_a_greyhound_can_eat:
        say = "Yes, a greyhound can eat {}.".format(food)

    reprompt = "What would you like to know? Ask away"
    should_end_session = False
    return response(session_attributes, speechlet_response(
        card_title, say, reprompt, should_end_session))


# --------------- Functions that control the skill's behavior ------------------

def welcome():
    session_attributes = {}
    card_title = "Welcome"
    say = "Hello. How are you? "
    reprompt = "What would you like to know? Ask away"
    should_end_session = False
    return response(session_attributes, speechlet_response(
        card_title, say, reprompt, should_end_session))


def goodbye():
    session_attributes = {}
    card_title = "Session Ended"
    say = "Thank you for speaking to me. " \
                    "Have a nice day! "
    should_end_session = True
    reprompt = None
    return response(session_attributes, speechlet_response(
        card_title, say, reprompt, should_end_session))


# --------------- Helpers ---------------

def value(intent, name):
    if intent['slots'][name]:
        return intent['slots'][name]['value'].lower()
    else:
        return None


def speechlet_response(title, say, reprompt, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': say
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': say
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt
            }
        },
        'shouldEndSession': should_end_session
    }


def response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
