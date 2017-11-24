import dog

def hello(event, context):
    """ handle Amazon Alexa events.

    routes the common Alexa request types to event methods.
    """

    for k, v in event.items():
        print(k, v)

    if event['session']['new'] == True:
        on_session_started(event['request'], event['session'])

    response = None
    if event['request']['type'] == "LaunchRequest":
        response = on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        intent_name = event['request']['intent']['name']
        if intent_name == "AMAZON.HelpIntent":
            response = on_help(event['request'], event['session'])
        elif intent_name == "AMAZON.CancelIntent":
            response = on_session_ended(event['request'], event['session'])
        elif intent_name == "AMAZON.StopIntent":
            response = on_session_ended(event['request'], event['session'])
#        elif event['request']['confirmationStatus'] == "NONE":
#            response = on_session_ended(event['request'], event['session'])
        else:
            response = on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        response = on_session_ended(event['request'], event['session'])

    return response

# --------------- Events ------------------

def on_session_started(request, session):
    print("on_session_started requestId=" + request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(request, session):
    return welcome()


def on_help(request, session):
    return welcome()


def on_session_ended(request, session):
    return goodbye()


def on_intent(request, session):
    intent = request['intent']
    name = intent['name']
    say = "not sure what to do with {}".format(name)
    print(intent['slots']['food'])
    if 'confirmationStatus' in intent['slots']['food']:
        return goodbye()
    if name == "CanItEat":
        say = can_it_eat(intent)
    session_attributes = {}
    card_title = name
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
    say = "Thank you for speaking to me. Have a nice day! "
    should_end_session = True
    reprompt = None
    return response(session_attributes, speechlet_response(
        card_title, say, reprompt, should_end_session))


def can_it_eat(intent):
    food = value(intent, 'food')
#    if "None" in food:
#        return goodbye()
    say = dog.can_eat(food)
    return say


# --------------- Helpers ---------------

def value(intent, name):
    try:
        return intent['slots'][name]['value'].lower()
    except KeyError:
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
