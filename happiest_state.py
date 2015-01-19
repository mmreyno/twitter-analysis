import json
import sys
from sys import argv
from collections import Counter

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

# state dictionary to compare to (in all caps)
states = {'VERMONT': 'VT', 'GEORGIA': 'GA', 'IOWA': 'IA', 'GUAM': 'GU', 'KANSAS': 'KS', 'FLORIDA': 'FL', 'VIRGINIA': 'VA', 'NORTH CAROLINA': 'NC', 'ALASKA': 'AK', 'NEW YORK': 'NY', 'CALIFORNIA': 'CA', 'MICHIGAN': 'MI', 'ALABAMA': 'AL', 'TEXAS': 'TX', 'IDAHO': 'ID', 'DELAWARE': 'DE', 'HAWAII': 'HI', 'ILLINOIS': 'IL', 'CONNECTICUT': 'CT', 'DISTRICT OF COLUMBIA': 'DC', 'MISSOURI': 'MO', 'NEW MEXICO': 'NM', 'PUERTO RICO': 'PR', 'OHIO': 'OH', 'MARYLAND': 'MD', 'ARKANSAS': 'AR', 'MASSACHUSETTS': 'MA', 'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'COLORADO': 'CO', 'MONTANA': 'MT', 'NEW JERSEY': 'NJ', 'UTAH': 'UT', 'NATIONAL': 'NA', 'WYOMING': 'WY', 'WASHINGTON': 'WA', 'MINNESOTA': 'MN', 'OREGON': 'OR', 'AMERICAN SAMOA': 'AS', 'VIRGIN ISLANDS': 'VI', 'SOUTH CAROLINA': 'SC', 'INDIANA': 'IN', 'NEVADA': 'NV', 'LOUISIANA': 'LA', 'NORTHERN MARIANA ISLANDS': 'MP', 'ARIZONA': 'AZ', 'WISCONSIN': 'WI', 'NORTH DAKOTA': 'ND', 'PENNSYLVANIA': 'PA', 'OKLAHOMA': 'OK', 'KENTUCKY': 'KY', 'RHODE ISLAND': 'RI', 'MISSISSIPPI': 'MS', 'NEBRASKA': 'NE', 'NEW HAMPSHIRE': 'NH', 'WEST VIRGINIA': 'WV', 'MAINE': 'ME'}
abbreviations = states.values()

# iterate over the tweets and get each word listed seperately
locations = {'MP': 0, 'PR': 0, 'GU': 0, 'MN': 0, 'CO': 0, 'ME': 0, 'WA': 0, 'VA': 0, 'UT': 0, 'VI': 0, 'CA': 0, 'DE': 0, 'DC': 0, 'WI': 0, 'AL': 0, 'WV': 0, 'AS': 0, 'HI': 0, 'VT': 0, 'IL': 0, 'GA': 0, 'IN': 0, 'IA': 0, 'MA': 0, 'MD': 0, 'AZ': 0, 'FL': 0, 'ID': 0, 'WY': 0, 'CT': 0, 'NH': 0, 'TN': 0, 'NJ': 0, 'MT': 0, 'OK': 0, 'NM': 0, 'TX': 0, 'OH': 0, 'AK': 0, 'NA': 0, 'MO': 0, 'NC': 0, 'ND': 0, 'NE': 0, 'OR': 0, 'KS': 0, 'NY': 0, 'PA': 0, 'AR': 0, 'MI': 0, 'MS': 0, 'LA': 0, 'SC': 0, 'KY': 0, 'RI': 0, 'NV': 0, 'SD': 0}
counter = {'MP': 0, 'PR': 0, 'GU': 0, 'MN': 0, 'CO': 0, 'ME': 0, 'WA': 0, 'VA': 0, 'UT': 0, 'VI': 0, 'CA': 0, 'DE': 0, 'DC': 0, 'WI': 0, 'AL': 0, 'WV': 0, 'AS': 0, 'HI': 0, 'VT': 0, 'IL': 0, 'GA': 0, 'IN': 0, 'IA': 0, 'MA': 0, 'MD': 0, 'AZ': 0, 'FL': 0, 'ID': 0, 'WY': 0, 'CT': 0, 'NH': 0, 'TN': 0, 'NJ': 0, 'MT': 0, 'OK': 0, 'NM': 0, 'TX': 0, 'OH': 0, 'AK': 0, 'NA': 0, 'MO': 0, 'NC': 0, 'ND': 0, 'NE': 0, 'OR': 0, 'KS': 0, 'NY': 0, 'PA': 0, 'AR': 0, 'MI': 0, 'MS': 0, 'LA': 0, 'SC': 0, 'KY': 0, 'RI': 0, 'NV': 0, 'SD': 0}
for l in range(0,num_lines):
    lowercase = []
    sentiment = 0
    place = []
    word_list = str(tweets[l].encode('utf-8')).split(' ') # splits each tweet into individual words
    for j in word_list:
        lowercase.append(j.lower()) # make lower case so it can be compared accurately
    for n in lowercase:
        try:
            sentiment = sentiment + scores[n] # gets the sentiment score of words in dictionary
        except KeyError:
            sentiment = sentiment + 0 # makes unknown words zero
        continue
    try:
        place = data[l]['user']['location'].encode('utf-8').split(' ') # split location into individual words
        for m in place:
            m.upper().strip() # make upper case to compare to our state dictionary
            if m in abbreviations:
                geolocation = m # we already have the state initial
            else:
                geolocation = states.get(m) # we find the shorthand for the full state name
        locations[geolocation] += sentiment # add locations to a dictionary with corresponding sentiment
        counter[geolocation] += 1
    except KeyError:
        deleted_tweets =  1 # BS to keep it running
    continue

for n in counter.keys():
    if counter[n] == 0: # need to remove division by zero
        counter[n] += 1
        
staterate = {k: float(locations[k])/counter[k] for k in counter.viewkeys() & locations.viewkeys()} # calculate happiness rating for each state

v = list(staterate.values())
k = list(staterate.keys())
print k[v.index(max(v))] # return the state with the highest rating
