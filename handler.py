def hello(event, context):
    """ handle Amazon Alexa events.

    routes the common Alexa request types to event methods.
    """

    if event['session']['new'] == True:
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
    name = intent['name']
    say = "not sure what to do with {}".format(name)
    if name == "CanItEat":
        say = can_it_eat(intent)
#        raise ValueError("Invalid intent")
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
    things_a_greyhound_can_eat = [
        'dog food',
        'kibbles'
    ]
    things_a_greyhound_shouldnt_eat = {
        'apple' : 'The seeds contain cyanogenic glycosides which can result in cyanide poisoning.',
        'apricot' : 'The seed pit contains cyanogenic glycosides which can cause cyanide poisoning.',
    }
    things_a_greyhound_mustnt_eat = {
        'alcohol' : 'Ingestion can lead to injury, disorientation, sickness, urination problems or even coma or death from alcohol poisoning',
        'anti-freeze' : 'Well yes, it can be deadly',
        'avocado' : 'Avocado contains a toxic element called persin which can damage heart, lung and other tissue in many animals. Avocadoes are high in fat content and can trigger an upset stomach, vomiting or even pancreatitis. The seed pit is also toxic and if swallowed can become lodged in the intestinal tract where it may cause a severe blockage which will have to be removed surgically. Since avocado is the main ingredient in guacamole be sure and keep your dog out of the dip.',
        'baby food' : 'Before feeding any baby food to your dog check the ingredients to see if it contains onion powder, which can be toxic to dogs. Feeding baby food in large amounts may result in nutritional deficiencies.',
        'bones' : 'Cooked bones can be very hazardous for your dog. Bones become brittle when cooked which causes them to splinter when broken. The splinters have sharp edges that have been known to become stuck in the teeth, caused choking when caught in the throat or caused a rupture or puncture of the stomach lining or intestinal tract. Especially bad bones are turkey and chicken legs, ham, pork chop and veal.',
        'bread dough' : 'your dog\'s body heat causes the dough to rise in the stomach which may give it bloat',
        'broccoli' : 'The toxic ingredient in broccoli is isothiocynate. While it may cause stomach upset it probably won\'t be very harmful unless the amount fed exceeds 10% of the dogs total dailey diet.',
        'caffeine' : 'Caffeine is a stimulant and can accelerate your pet\'s heartbeat to a dangerous level. Pets ingesting caffeine have been known to have seizures, some fatal.',
        'candy' : 'Sugarless candy containing xylitol can be a risk to pets',
        'cat food' : 'Cat food is not formulated for canine comsumption. It is generally too high in protein and fats and is not a balanced diet for a dog.',
        'cherries' : 'The seed pit contains cyanogenic glycosides which can cause cyanide poisoning.',
        'chocolate' : 'Chocolate contains theobromine, which a cardiac stimulant and a diuretic. An overdose of chocolate can make a dog excited and hyperactive. It may pass large volumes of urine and be unusually thirsty. Vomiting and diarrhea are also common. Theobromine will either increase the dog’s heart rate or may cause the heart to beat irregularly. Death is quite possible, especially with exercise. Symptoms of chocolate poisoning include: vomiting, diarrhea, tremors, hyperactivity, irregular heartbeat and seizures.',
    }
    food = value(intent, 'food')
    say = "I am not sure about {}".format(food)
    if food in things_a_greyhound_mustnt_eat:
        say = "No, a greyhound must not eat {}. {}".format(food, things_a_greyhound_mustnt_eat[food])
    if food in things_a_greyhound_shouldnt_eat:
        say = "A greyhound should not eat {}. {}".format(food, things_a_greyhound_shouldnt_eat[food])
    elif food in things_a_greyhound_can_eat:
        say = "Yes, a greyhound can eat {}.".format(food)
    return say


# --------------- Helpers ---------------

def value(intent, name):
    try:
        return intent['slots'][name]['value'].lower()
    except ValueError:
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
