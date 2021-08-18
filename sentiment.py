#Checking when do people make mistakes the most when talking about specific topics

#Example: Batman vs Superman
#Superman tweets have more spelling errors, hence Superman fans are dumb
import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from textblob import Word
from secrets import consumer_key, consumer_secret,access_token_key,access_token_secret

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
api=tweepy.API(auth)



def get_tweets(keyword: str)->List[str]:
    all_tweets=[]
    for tweet in tweepy.Cursor(api.search,q=keyword,tweet_mode='extended',lang='en').items(10
):
        all_tweets.append(tweet.full_text)
    return all_tweets


def cleanup_tweets(all_tweets1: List[str])->List[str]:
    tweets_clean=[]
    for tweet1 in all_tweets1:
        tweets_clean.append(p.clean(tweet1))
    return tweets_clean

def get_sentiment(all_tweets2: List[str])->List[float]:
    sentiment_scores=[]
    for tweet1 in all_tweets2:
        blob=TextBlob(tweet1)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores


def get_spelling_mistakes(all_tweets:List[str])->List[float]:
    spelling_scores=[]
    for tweet1 in all_tweets:
        blob=TextBlob(tweet1)
        word_collection=blob.words
        for w in word_collection:
            test_word=Word(w)
            t=(test_word.spellcheck())
            k,l=zip(*t)
            l=l[0]
            if(l==1.0):
                spelling_scores.append(1.0)
    return spelling_scores
    

def get_score1(keyword: str)->int:
    tweets=get_tweets(keyword)
    tweets_cleaned=cleanup_tweets(tweets)
    spelling_scored=get_spelling_mistakes(tweets_cleaned)
    return len(spelling_scored)

def get_score(keyword: str)->int:
    tweets=get_tweets(keyword)
    tweets_cleaned=cleanup_tweets(tweets)
    sentiment_scored=get_sentiment(tweets_cleaned)
    return statistics.mean(sentiment_scored)



str1="Ben Shapiro"
str2="Joe Biden"

print("Spellings for Shapiro ")
print(get_score1(str1))
print("Spellings for Biden ")
print(get_score1(str2))
if get_score(str1)>get_score(str2):
    print(str1+" kicks the ass of "+str2)
else:
    print(str2+" kicks the ass of "+str1)


