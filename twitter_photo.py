import tweepy
import json


with open("twitter_credentials.json", "r") as read_file:
    cred = json.load(read_file)

with open("users.json", "r") as read_file:
    users = json.load(read_file)

auth = tweepy.OAuthHandler(cred['CONSUMER_KEY'], cred['CONSUMER_SECRET'])
auth.set_access_token(cred['ACCESS_TOKEN'], cred['ACCESS_SECRET'])

api = tweepy.API(auth)

user = api.get_user(users['user1'])

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)

