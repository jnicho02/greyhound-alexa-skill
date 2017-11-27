# greyhound-alexa-skill
An Amazon Alexa skill that advises greyhound owners on what their dog can eat

# to setup
```sh
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

to send Alexa events to S3:
```sh
export LOGEVENTS=true
```

# to test
py.test tests/test_handler.py

#to deploy
```sh
sls deploy
```
