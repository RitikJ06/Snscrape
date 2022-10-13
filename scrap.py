import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list = []

# put this in another for loop to get the replies for all url
# 1580354944594456576 is the tweet id that you can extract from the url you have
for i,tweet in enumerate(sntwitter.TwitterTweetScraper(1580354944594456576, mode=sntwitter.TwitterTweetScraperMode.RECURSE).get_items()):
    tweets_list.append([tweet.id, tweet.user.username, tweet.content, tweet.date])
    
tweets_df2 = pd.DataFrame(tweets_list, columns=['Tweet_ID', 'Username', 'Tweet_Text', 'Datetime'])
print(len(tweets_list))
for t in tweets_list:
    print(t)

