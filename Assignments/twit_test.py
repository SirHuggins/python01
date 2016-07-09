import tweepy

consumer_key='rDsfdRCpmCecpNZqp5QyPHXcH',
consumer_secret='MU7EYfCJv6hAG1RqnXOpxVDePR590cBMuC7201wi1Y302gGQKl'
access_token_key='3371670279-2L9gSKGjnxL0n11eKIgmJMccJbiB3G52wTmxfS0'
access_token_secret='2Wl3gTGl39qLRN6js4FAdnbkwh6OMN69hmbrLOEi0O6b8'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text