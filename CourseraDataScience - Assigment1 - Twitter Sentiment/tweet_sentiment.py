import sys
import json

def hw():

    print('Hello, world!')

def lines(fp):

    print(str(len(fp.readlines())))
    return len(fp.readline())

def main():

    hw()
    lines(sent_file)
    lines(tweet_file)

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
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
    sentiment = []
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for tweet in Tweets:
        weight = 0
        tweetText = tweet.get('text')
        if tweetText != None:
            tweetTextSplited = tweetText.split()

            for i in tweetTextSplited:
                if i in scores:
                    weight = weight + int(scores[i])
        else:

            weight = weight + 0

        sentiment.append(weight)

    for i in sentiment:
        print(str(i) + '\n')


if __name__ == '__main__':
    main()



