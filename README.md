This is a documentation of the Insight Data Engineer challenge - September program in NYC.

Insight Data Engineering - Coding Challenge:
Develop tools that could help analyze the community of Twitter users. For simplicity, the features we will build are primitive, but you could easily build more complicated features on top of these.

Challenge Summary

This challenge is to implement two features:
  1) Calculate the total number of times each word has been tweeted.
  2) Calculate the median number of unique words per tweet, and update this median as tweets come in.

Here is the breakdown of the repository files:

  ├── README.md  
  ├── run.sh  
  ├── src  
  │   ├── median_unique.py  
  │   └── words_tweeted.py  
  ├── tweet_input  
  │   └── tweets.txt  
  └── tweet_output  
      ├── ft1.txt  
      └── ft2.txt  

About the Solution:

1) The solution was created using Python
2) The soution is found in a file named src.

    - words_tweeted.py 
    The program attempts to do the following: (imports sys)
    1) Open the tweets.txt text file. 
    2) It then goes to each line in the text and splits it into words (after each space it counts as a word).
    3) The wordDictionary set adds new words into its set. There is a conditional in this solution. The IF conditional checks whether or not a a word has been already added to the set or not.
    4) It then closes the tweet.txt
    5) At the end, the program prints each word in the tweet that's found in wordDictionary set and its fequency into ft1.txt then closes the file.
    
    - median_unique.py
    The program attempts to do the following:
    1) IT checks which system the user is using and dpending on that it imports the proper library that works for the system.
    2) Open the tweets.txt test file.
    3) It then goes to each line in the text and splits it into words (after each space it counts as a word).
    4) It takes each line and splits it into words and appends it to wordsPerTweet.
    5) It performs the statistics.median calculation on wordsPerTweet and appends it to medianNumberOfWords and closes the file it was reading from (tweet.txt).
    6) At the end, it converts the values of medianNumberOfWords into strings and outputs the median calculated and prints them into ft2.txt.

  Environment developed in:
  I used Python 3 and developed the code in IDLE. I ran the code using Python 3 Shell, cmd, Linux.
  I have then modified the code to make it runable using run.sh and tested it using linux.
  
  Environments where the solution was tested:
  Python 3 Shell, cmd, and ran run.sh in Linux.
