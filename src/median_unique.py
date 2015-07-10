# example of program that calculates the median number of unique words per tweet.
import statistics

wordsPerTweet = []
medianNumberOfWords = []
tweet = open("tweets.txt","r")
for line in tweet:
    tweetWords = line.split()
            
    wordsPerTweet.append(len(line.split()))
    medianNumberOfWords.append(statistics.median(wordsPerTweet))

print("The median is: " +str(medianNumberOfWords))

