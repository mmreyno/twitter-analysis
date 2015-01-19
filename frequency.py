import json
import sys
from sys import argv
from collections import Counter

twitter_data = open(sys.argv[1])
data = [json.loads(line) for line in twitter_data] # get ALL our data into a big ass list
num_lines = len(open(sys.argv[1]).readlines(  ))    # find the number of lines in the file

tweets = []


for i in range(0,num_lines):
    try:
        tweets.append(data[i]['text']) # extract only the tweets from all the junk
    except KeyError:
        tweets.append('goobledeegook') # give it some nonsense if the tweet was deleted, so score will be 0
    continue

# iterate over the tweets and get each word listed seperately
allwords = []
for l in range(0,num_lines):
    lowercase = []
    word_list = str(tweets[l].encode('utf-8')).split(' ')   # splits each tweet into individual words
    for j in word_list:
        lowercase.append(j.lower().strip()) # make lower case so it can be compared accurately
    for k in lowercase:
        allwords.append(k)  # put every word into a big ass list

# remove our placeholder
placeholder = 'goobledeegook'
while placeholder in allwords:
    allwords.remove(placeholder)

number_of_words = float(len(allwords))  # get the number of words in the list
freq_dictionary = dict(Counter(allwords))   # turn the counter into a dictionary we can use

for k,v in freq_dictionary.items():
    print k,v/number_of_words   # print pairs, dividing the frequency of one word by the total number of words there are
