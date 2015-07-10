# example of program that calculates the total number of times each word has been tweeted.
WordDictionary = {}

tweet = open("../tweet_input/tweets.txt","r")
for line in tweet:
    tweetWords = line.split()
    for word in tweetWords:
        if word in WordDictionary:
            WordDictionary[word]+=1
        else:
            WordDictionary[word] = 1

for word, frequency in WordDictionary.items():
    print(word + "\t\t\t" + str(frequency))
