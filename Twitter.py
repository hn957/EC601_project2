from requests_oauthlib import OAuth1Session
import os
import json
import sys


 
# Invokation Argument --
n = len(sys.argv)
 
# Checking if argument provided is correct --
if n < 5:
    print("Syntax:\t\tmain.py search_query expected_json_filename count_of_required_no_of_tweet hashtag_or_user\nFor Example:\tmain.py apple apple.json 100 hashtag")
    exit()
 


# Checking if user inputs wrong parameter at 4th place
if not (sys.argv[4] == "hashtag" or sys.argv[4] == "user"):
    print("Syntax:\t\tmain.py search_query expected_json_filename count_of_required_no_of_tweet hashtag_or_user\nFor Example:\tmain.py apple apple.json 100 hashtag")
    exit()
search_type = sys.argv[4]


 
# Adding File Extension if end-user forgets/doesn't adds --
if not sys.argv[2].endswith(".json"):
    sys.argv[2] = sys.argv[2] + ".json"
expected_json_file_name = sys.argv[2]
 


# API Key Configuration --
CONSUMER_KEY = "XXXXXXXXXXXXXXXXXXXXXX" # API Key
CONSUMER_SECRET = "XXXXXXXXXXXXXXXXXXXXXX" # API Secret
ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXXXXXXXXXXX"

 
# API Endpoint for Standard Search --
SEARCH_URL = 'https://api.twitter.com/1.1/search/tweets.json'
 
def search(params):
    twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    req = twitter.get(SEARCH_URL, params = params)
    tweets = json.loads(req.text)
    return tweets


 
# Parsing the parameter --
def parseToParam(parse_str, parse=None):
    if parse is None:
        parse = '&'
    return_params = {}
    parsed_str = parse_str.split(parse)
    for param_string in parsed_str:
        param, value = param_string.split('=', 1)
        return_params[param] = value
    return return_params


 
def main():

    # Adding respective identifier to the search query --
    if search_type == "hashtag":
        search_word = '#' + sys.argv[1]
    else:
        search_word = '@' + sys.argv[1]
    tweet_data = []
 
    # Standard Search Configuration --
    params = {
                'q'  : search_word,
                'count'  : 100,
             }
    tweet_count = 0
 
    while tweet_count < int(sys.argv[3]):
        tweets = search(params)
        for tweet in tweets['statuses']:
            tweet_data.append(tweet)
            
        # Parsing parameter tweets['search_metadata']['next_results']
        if 'next_results' in tweets['search_metadata'].keys():
            next_results = tweets['search_metadata']['next_results']
            next_results = next_results.lstrip('?') # Removing ? from beginning of delete
            params = parseToParam(next_results)
            # Replacing the modified qry %Added 25
            params['q'] = params['q'].replace('%25', '%') 
            tweet_count += len(tweets['statuses'])
        else:
            break
 
    # Storing json to file --
    with open(expected_json_file_name, "w") as outfile:
        json.dump(tweet_data, outfile)
 
    print("Successfully saved " + str(tweet_count) + " tweets!\nFilename: " + expected_json_file_name)
 
if __name__=='__main__':
    main()