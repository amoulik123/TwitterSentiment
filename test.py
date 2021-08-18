from textblob import TextBlob
import tweepy
import preprocessor as p
import statistics
from typing import List
from textblob import Word




def func():
    animals = TextBlob("cat dog india")
    words=animals.words
    scores=[]
    for word in words:
        w=Word(word)
        t=(w.spellcheck())
        k,l=zip(*t)
        l=l[0]
        print(l)
        
    
    return scores

func()