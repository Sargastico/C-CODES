import sys
import json
import collections

def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))
    return len(fp.readline())

def main():

    TweetFile = open(str(sys.argv[1]))
    # TweetFile = open('three_minutes_tweets.json')

    List = []

    for line in TweetFile:
        pyResponse = json.loads(line)
        try:
            hashData = pyResponse['entities']['hashtags']
        except:
            pass
        try:
            hashtags = hashData[0]['text']
            List.append(hashtags)
        except:
            pass

    counter = collections.Counter(List)
    mostCommon = counter.most_common()
    for i in range(10):
        print(mostCommon[i][0], mostCommon[i][1])


if __name__ == '__main__':
    main()