import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('forest fire since:2021-07-01 until:2021-12-31').get_items()):
    if i>10:
        break
    tweets_list2.append([tweet.id, tweet.user.username, tweet.content, tweet.date])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Tweet_ID', 'Username', 'Tweet_Text', 'Datetime'])
for t in tweets_list2:
    print(t)

