import requests
import time

##
#
# MODIFY THESE VARIABLES
# CONTENT URI is a link to the recording you are hoping to process. This is going to be a path from the webhook step, for example (
#
CONTENT_URI = pd.steps["trigger"]["event"]["recording"]["contentUri"]) 
ASSEMBLY_RECEIVE_WEBHOOK = "Insert the URI for your second webhook here"
ASSEMBLY_AI_KEY = "Insert your API key here" 

def handler(pd: "pipedream"):
  #
  #
  #
  audio_file = CONTENT_URI

  endpoint = "https://api.assemblyai.com/v2/transcript"
  json = {
    "audio_url": audio_file,
    "sentiment_analysis": True,
    "summarization": True,
    "webhook_url": ASSEMBLY_RECEIVE_WEBHOOK,
    "summary_type": "bullets"
  }
  headers = {
    "authorization": ASSEMBLY_AI_KEY,
    "content-type": "application/json"
  }
  response = requests.post(endpoint, json=json, headers=headers)
  response_json = response.json()
