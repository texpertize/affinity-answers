# Degree Of Profanity Computation For Twitter Tweets
import re

"""The program first reads in the set of racial slurs from the file "racial_slurs.txt" 
and stores them in a set for efficient searching."""
"""It then reads in the tweets from the file "tweets.txt" and stores them in a list.
For each tweet, it calls the "get_degree_of_profanity" function, which checks if any of the racial slurs are present in the tweet.
If a slur is present, the function returns a degree of profanity of 1, otherwise it returns 0. """

def get_degree_of_profanity(tweet, racial_slurs):
    tweet = tweet.lower()
    for slur in racial_slurs:
        if re.search(r'\b{}\b'.format(slur), tweet):
            return 1
    return 0

if __name__ == '__main__':
    with open('racial_slurs.txt', 'r') as f:
        racial_slurs = set([line.strip() for line in f])

#The program then creates a list of tuples, where each tuple contains the tweet and its degree of profanity.
    tweets = []
    with open('tweets.txt', 'r') as f:
        for line in f:
            tweets.append(line.strip())
    
    tweet_degrees = [(tweet, get_degree_of_profanity(tweet, racial_slurs)) for tweet in tweets]

 #The list is sorted in descending order of profanity using the "sort" method with a lambda function as the key.
   
    tweet_degrees.sort(key=lambda x: x[1], reverse=True)
    
    for tweet, degree in tweet_degrees:
        print('{}\t{}'.format(tweet, degree))

#Finally, the program prints out each tweet and its degree of profanity.