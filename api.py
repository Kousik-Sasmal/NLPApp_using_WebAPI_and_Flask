import paralleldots

paralleldots.set_api_key('9jshsaRrZSJnQYfy7uZrBG7s2cz5XjjU3n5vZp6uB7I')

def ner(text):
    ner_resp = paralleldots.ner(text)
    return ner_resp

def sentiment(text):
    sentiment_resp = paralleldots.sentiment(text)
    return sentiment_resp

def abuse(text):
    abuse_resp = paralleldots.abuse(text)
    return abuse_resp

def emotion(text):
    emotion_resp = paralleldots.emotion(text)
    return emotion_resp

