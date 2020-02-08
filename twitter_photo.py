import tweepy
import json
import csv


with open("twitter_credentials.json", "r") as read_file:
    cred = json.load(read_file)

with open("users.json", "r") as read_file:
    users = json.load(read_file)

auth = tweepy.OAuthHandler(cred['CONSUMER_KEY'], cred['CONSUMER_SECRET'])
auth.set_access_token(cred['ACCESS_TOKEN'], cred['ACCESS_SECRET'])

api = tweepy.API(auth)

csvfile = open("tweet.csv", "w", newline="")
csvwriter = csv.writer(csvfile)

# all page crawl
for timeline in tweepy.Cursor(api.user_timeline, id=users['user2']).pages():
    for tweet in timeline:
        try:           
            csvwriter.writerow([tweet._json['text'], tweet._json['extended_entities']['media'][0]['media_url']])        
        except (KeyError, AttributeError):
            pass


# first page crawl
# timeline = api.user_timeline(id=users['user2'])
# for tweet in timeline:
#         try:                
#             csvwriter.writerow([tweet._json['text'], tweet._json['extended_entities']['media'][0]['media_url']])
#         except (KeyError, AttributeError):
#             pass
