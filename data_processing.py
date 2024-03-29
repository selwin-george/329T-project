import pandas as pd
import subprocess 

subprocess.call(
    ["wget", "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"]
)
subprocess.call(
    ["unzip", "trainingandtestdata.zip"]
)

# Reading in sentiment140 dataset
df = pd.read_csv("training.1600000.processed.noemoticon.csv",
                names=['polarity', 'id', 'date', 'query', 'user', 'text'],
                encoding='latin-1')

tweet_sentiment_pairs = df[['text','polarity']]
tweet_sentiment_pairs['polarity'] //= 4
tweet_sentiment_pairs.rename(columns = {'polarity':'sentiment'}, inplace = True)

# Write csv of text, sentiment pairs (0 negative, 1 positive)
tweet_sentiment_pairs.to_csv('tweet_sentiment_pairs.csv')
