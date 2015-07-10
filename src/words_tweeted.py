# example of program that calculates the total number of times each word has been tweeted.

import sys
inputFile = sys.argv[1]
outputFile = sys.argv[2]

WordDictionary = {}

tweet = open(inputFile,"r")
for line in tweet:
    tweetWords = line.split()
    for word in tweetWords:
        if word in WordDictionary:
            WordDictionary[word]+=1
        else:
            WordDictionary[word] = 1

tweet.close()

ft1 = open(outputFile,"w")
for word, frequency in WordDictionary.items():
    ft1.write(word+" "+str(frequency)+"\n")

ft1.close()

print("words_tweeted.py ran successfully! Please check the output file"+outputFile)
