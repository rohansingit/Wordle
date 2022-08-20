import tweepy
from textblob import TextBlob
consumer_key = 'LtEkZ3NRfKqFFvv0myOZK0qYr'
consumer_secret = 'EjFUXiQKcqBLbfAbmbo3r89xiRp7ztfhK191kNiiqF4vYi8qwQ'

access_token = '1266933402239930373-u06oQLJZpVl0XBTQ7BYfsfLHbkztZt'
access_token_secret = 'A4cx4mFgLRH299Md4pNZCld8XlsKEeZGk5nYungcrSJ5X'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('sad')
tweet_amount = 70
tweet_polarity = 0

tweets = tweepy.Cursor(api.search_tweets, q = public_tweets, lang = 'en').items(tweet_amount)
polarity = 0
positive = 0
negative = 0
neutral = 0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    final_text = tweet.text.replace('RT', ' ')
    if final_text.startswith(' @'):
      position = final_text.index(':')
      final_text = final_text[position+2:]
    if final_text.startswith('@'):
      position = final_text.index(' ')
      final_text = final_text[position+2:]
      analysis = TextBlob(final_text)
      tweet_polarity = analysis.polarity
      polarity += analysis.polarity
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
         negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += tweet_polarity
    



print(polarity)
print (f'Amount of positive tweets: {positive}')
print (f'Amount of negative tweets: {negative}')
print (f'Amount of neutral tweets: {neutral}')
