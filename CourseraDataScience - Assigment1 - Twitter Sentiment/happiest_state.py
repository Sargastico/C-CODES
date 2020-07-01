import operator
import sys
import json

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))
    return len(fp.readline())


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # sent_file = open('AFINN-111.txt')
    # tweet_file = open('three_minutes_tweets.json')

    hw()
    lines(sent_file)
    lines(tweet_file)

    with open("three_minutes_tweets.json", "r") as read_file:
        Tweets = []
        file_lines = read_file.readlines()
        for line in file_lines:
            # if type(line) != type(None):
            Tweets.append(json.loads(line))

    afinnfile = open("AFINN-111.txt")
    scores = {}
    mapStates = {}

    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for tweet in Tweets:

        tweetText = tweet.get('text')
        tweetPlace = tweet.get('place')

        if tweetPlace != None:

            stateInTweet = tweetPlace['full_name']
            tweetCountryCode = tweetPlace['country_code']

            if tweetText != None:
                tweetTextSplited = tweetText.split()
                for words in tweetTextSplited:
                    if words in scores:
                        if tweetCountryCode == 'US':

                            if type(stateInTweet) == list:
                                stateInTweet = ','.join(stateInTweet)

                            stateInTweet = stateInTweet.split(',')

                            if len(stateInTweet) == 2:

                                stateInTweetDos = stateInTweet[1]

                            else:
                                stateInTweet = 'US Misc'

                            stateInTweet = ''.join(stateInTweet)

                            if stateInTweetDos in mapStates:
                                mapStates[stateInTweetDos] = + int(scores[words])

                            else:
                                mapStates[stateInTweetDos] = int(scores[words])

    print(mapStates)
    print(max(mapStates.items(), key=operator.itemgetter(1))[0])


if __name__ == '__main__':
    main()
