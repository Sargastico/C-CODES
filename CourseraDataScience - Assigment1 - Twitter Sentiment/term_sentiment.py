import sys
import json

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():

    # sent_file = open(sys.argv[1])
    # tweet_file = open(sys.argv[2])

    sent_file = open('AFINN-111.txt')
    tweet_file = open('three_minutes_tweets.json')
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

    scores = {}  # initialize an empty dictionary
    sentiment = {}
    newTerms = {}
    sentimentByTweet = {}

    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for tweet in Tweets:

        tweetID = tweet.get('id')
        tweetText = tweet.get('text')
        tweetLang = tweet.get('lang')

        weight = 0
        if tweetLang == 'en':
            if tweetText != None:
                tweetTextSplited = tweetText.split()

                for i in tweetTextSplited:
                    if i in scores:
                        weight = weight + int(scores[i])
                        if i != '':
                            sentiment[i] = weight
                            sentimentByTweet[tweetID] = float(weight)
            else:
                sentimentByTweet[tweetID] = float(weight)


    for tweet in Tweets:
        tweetLang = tweet.get('lang')
        tweetID = tweet.get('id')
        tweetText = tweet.get('text')

        if tweetLang == 'en':
            if tweetText != None:
                tweetTextSplited = tweetText.split()

                for word in tweetTextSplited:
                    word = word.strip('?:!.,;"!@')
                    word = word.replace("\n", "")
                    if word not in sentiment.keys():
                        if tweetID in sentimentByTweet.keys():
                            if word not in newTerms:
                                newTerms[word] = (sentimentByTweet[tweetID])
                            else:
                                newTerms[word] = newTerms[word] + sentimentByTweet[tweetID]

    for word in newTerms:
        if newTerms[word] > 10:
            newTerms[word] = newTerms[word]/10

    print(newTerms)

if __name__ == '__main__':
     main()
