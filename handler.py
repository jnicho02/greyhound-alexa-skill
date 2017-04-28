import json

def hello(event, context):
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
