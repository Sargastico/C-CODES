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
            Tweets.append(json.loads(line))

    CountMap = {}
    FreqMap = {}


    for tweet in Tweets:
        tweetLang = tweet.get('lang')
        tweetText = tweet.get('text')

        if tweetLang == 'en':
            if tweetText != None:
                tweetTextSplited = tweetText.split()

                for word in tweetTextSplited:
                    word = word.strip('?:!.,;"!@')
                    word = word.replace("\n", "")
                    if word in CountMap:
                        CountMap[word] += 1
                    else:
                        CountMap[word] = 1

    for termo in CountMap:

        numTermOcurrs = CountMap[termo]
        sumOfAllTerms = sum(CountMap.values())
        FreqMap[termo] = numTermOcurrs/sumOfAllTerms

    print(FreqMap)

if __name__ == '__main__':
     main()
