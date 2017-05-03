# greyhound-alexa-skill
An Amazon Alexa skill that advises greyhound owners

# to setup
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

# to test
py.test tests/test_handler.py
