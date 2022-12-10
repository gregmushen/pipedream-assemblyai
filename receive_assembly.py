import requests


# USER INPUT VARIABLES
# 
ASSEMBLY_AI_KEY="INSERT YOUR KEY HERE"

def handler(pd: "pipedream"):
  transcript_id = transcription_id = pd.steps["trigger"]["event"]["body"]["transcript_id"]
  endpoint = "https://api.assemblyai.com/v2/transcript/" + transcript_id
  headers = {
    "authorization": ASSEMBLY_AI_KEY,
  }
  response = requests.get(endpoint, headers=headers)
  response_json = response.json()
  sentiment_analysis = response_json["sentiment_analysis_results"]
  sentiment_neutral = 0
  sentiment_positive = 0
  sentiment_negative = 0
  for sentiment in sentiment_analysis:
    if sentiment["sentiment"] == "NEUTRAL":
      sentiment_neutral += 1
    elif sentiment["sentiment"] == "POSITIVE":
      sentiment_positive += 1
    elif sentiment["sentiment"] == "NEGATIVE":
      sentiment_negative += 1

  if sentiment_negative != 0:
    sentiment = "NEGATIVE"
  else:
    sentiment = "OK"
  
  print(response_json)

  return { "summary": response_json["summary"], "sentiment": sentiment, "audio_url": response_json["audio_url"] }
