import tweepy
import pandas as pd
import configparser


# read configuration

config = configparser.ConfigParser()
config.read('config.ini')

API_Key = config['Twitter']['API_Key']
API_Secret = config['Twitter']['API_Key_Secret']
acessToken = config['Twitter']['access_token']
acessSecretToken = config['Twitter']['access_secret_token']

# print(API_Key, API_Secret, acessToken, acessToken)

auth = tweepy.OAuth1UserHandler(API_Key,API_Secret)

auth.set_access_token(acessToken,acessSecretToken)

api = tweepy.API(auth)

numberOfTweets = 100

# cursor = tweepy.Cursor(api.user_timeline,id='@CNN',tweet_mode="extended").items(numberOfTweets)

tweetText = []
tweetLikes = []
time = []

# printing data
# for i in cursor:
#     tweetText.append(i.full_text)
#     tweetLikes.append(i.favorite_count)
#     time.append(i.created_at)

# df = pd.DataFrame({'Tweet Text': tweetText,'Likes': tweetLikes,'Time': time})

# df.to_csv('CNN.csv')

# part 2

# api search for covid 
cursor = api.search_tweets(q="covid",lang="en",count=numberOfTweets,tweet_mode="extended")

for i in cursor:
    tweetText.append(i.full_text)
    tweetLikes.append(i.favorite_count)
    time.append(i.created_at)
    # print(i)

df = pd.DataFrame({'Tweet Text': tweetText,'Likes': tweetLikes,'Time': time})

df.to_csv('covidNews.csv')