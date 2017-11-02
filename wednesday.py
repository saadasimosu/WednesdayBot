import requests
import json
import time

# Bot paramaters
bot_id = 
image_url =
headers =
message =

# Construct data objects
image_data = {'bot_id':bot_id,'picture_url':image_url}
message_data = {'bot_id':bot_id,'text':message}

# Serialize objects to JSON formatted String
image_data_json = json.dumps(image_data)
message_data_json = json.dumps(message_data)


# POST image request to bot
try:
    r = requests.post('https://api.groupme.com/v3/bots/post', data = image_data_json, headers = headers, verify=True)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print e
    sys.exit(1)

time.sleep(10)

# POST image request to bot
try:
    r = requests.post('https://api.groupme.com/v3/bots/post', data = message_data_json, headers = headers, verify=True)
except requests.exceptions.RequestException as e:  # This is the correct syntax
    print e
    sys.exit(1)
