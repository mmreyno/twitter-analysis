import json
import sys
from sys import argv
from collections import Counter

twitter_data = open(sys.argv[1])
data = [json.loads(line) for line in twitter_data] # get ALL our data into a big ass list
num_lines = len(open(sys.argv[1]).readlines(  ))    # find the number of lines in the file

hashtags = []

for i in range(0,num_lines):
    try:
        taglist = (data[i]['entities']['hashtags']) # access hashtags of the tweets
        for n in range(0,len(taglist)):
            hashtags.append(taglist[n]['text']) # get text of hashtags
    except KeyError:
        missing_tweets = 1 # ignore deleted tweets
    continue

# make all tags lowercase
lowercase = []
for l in range(0,len(hashtags)):
    lowercase.append(hashtags[l].encode('utf-8').lower())  # encode as utf-8 and make lowercase

# find the top 10 most common by using Counter
for k,v in Counter(lowercase).most_common(10):
    print k, v   # print pairs, dividing the frequency of one word by the total number of words there are
