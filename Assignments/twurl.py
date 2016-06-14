import urllib
import oauth
import hidden

def augment(url, parameters) :
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['4Lbk2LfVeO4HdECisAxQxG57j'], secrets['Yu1F25HoGKYgbedlugmrBYwp78clegb41TyY0P55Fe7eFYuwys'])
    token = oauth.OAuthToken(secrets['3371670279-2L9gSKGjnxL0n11eKIgmJMccJbiB3G52wTmxfS0'],secrets['2Wl3gTGl39qLRN6js4FAdnbkwh6OMN69hmbrLOEi0O6b8'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, 
        token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()


def test_me() :
    print '* Calling Twitter...'
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'drchuck', 'count': '2'} )
    print url
    connection = urllib.urlopen(url)
    data = connection.read()
    print data
    headers = connection.info().dict
    print headers
