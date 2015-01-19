import json
import sys
from sys import argv

twitter_data = open(sys.argv[2])
data = [json.loads(line) for line in twitter_data] # get our data into a big ass list
num_lines = len(open(sys.argv[2]).readlines(  ))

tweets = []

for i in range(0,num_lines):
    try:
        tweets.append(data[i]['text']) # extract only the tweets from all the junk
    except KeyError:
        tweets.append('goobledeegook') # give it some nonsense if the tweet was deleted, so score will be 0
    continue

# opens the scoring rubric and turns it into a dictionary
afinnfile = open(sys.argv[1])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

# iterate over the tweets and get each word listed seperately
for l in range(0,num_lines):
    lowercase = []
    sentiment = 0
    word_list = str(tweets[l].encode('utf-8')).split(' ') # splits each tweet into individual words
    #print word_list
    for j in word_list:
        lowercase.append(j.lower()) # make lower case so it can be compared accurately
    for k in lowercase:
        try:
            sentiment = sentiment + scores[k]
        except KeyError:
            sentiment = sentiment + 0
        continue
    print sentiment

