# example of program that calculates the median number of unique words per tweet.
try:
    import statistics
    from statistics import median
except ImportError:
    print("So you're a Linux user...ok let's continue!")
    
try:
    import numpy
    from numpy import median
except ImportError:
    print("So you're a Windows user..ok let's continue!")

import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

wordsPerTweet = []
medianNumberOfWords = []

tweet = open(inputFile,"r")
for line in tweet:
    tweetWords = line.split()
            
    wordsPerTweet.append(len(line.split()))
    medianNumberOfWords.append(median(wordsPerTweet))

tweet.close()
ft2 = open(outputFile,"w")

ft2.write("The medians are: " +str(medianNumberOfWords))

ft2.close()

print("median_unique.py ran successfully! Please check the output file"+outputFile)
