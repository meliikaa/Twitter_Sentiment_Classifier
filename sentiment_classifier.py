# -*- coding: utf-8 -*-
"""sentiment classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16Hpo2EFZ7Q059zVGrGfc7HkNtqBr4FJo

To start this project :
Firstly, defined a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word
"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (str1):
    for i in range (9):
        str1 = str1.replace(punctuation_chars[i], "")
    strip_punctuation = str1
    return strip_punctuation

"""In second step, copied in my strip_punctuation function and defined a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Used the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so I convertd all the words in the input string to lower case as well. Moreover, I also used strip_punctuation to get ride of any extra character in the string."""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
def strip_punctuation (str1):
    for i in range (9):
        str1 = str1.replace(punctuation_chars[i], "")
    strip_punctuation = str1
    return strip_punctuation

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
        
def get_pos(str2):
    global pos_count
    pos_count = 0
    str2 = str2.lower()
    words = strip_punctuation(str2).split()
    for word in words:
        if word in positive_words:
            pos_count += 1
    return pos_count

"""The above step was also done for negative_words"""

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (str1):
    for i in range (9):
        str1 = str1.replace(punctuation_chars[i], "")
    strip_punctuation = str1
    return strip_punctuation

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(str2):
    global neg_count
    neg_count = 0
    str2 = str2.lower()
    words = strip_punctuation(str2).split()
    for word in words:
        if word in negative_words :
            neg_count += 1
    return neg_count

"""opened the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). the original task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Now, we will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order.

```
# match = re.search(r'(\d+),(\d+)$', input_str)
num1 = int(match.group(1))
num2 = int(match.group(2))
```

This piece of code uses the re module in Python to search for a pattern in a string using regular expressions.

The regular expression pattern (\d+),(\d+)$ is looking for a sequence of one or more digits \d+, followed by a comma ,, and then another sequence of one or more digits \d+, followed by the end of the string $.

re.search searches the string for the given pattern, and if it finds a match, it returns a MatchObject which can be used to extract the matched parts of the string.

match.group(1) extracts the first matched group (the first sequence of digits before the comma) as a string, and int(match.group(1)) converts it to an integer. Similarly, match.group(2) extracts the second matched group (the second sequence of digits after the comma) as a string and converts it to an integer.
*italicized text*
So essentially, this code is extracting two numbers that are at the end of a string separated by a comma, and storing them as num1 and num2. *italicized text*

```
input_str = input_str[:-len(match.group(0))]
```

The line input_str = input_str[:-len(match.group(0))] removes the matched portion of the string from input_str.

Here's how it works:

1-match.group(0) returns the entire matched string, which is the last comma-separated pair of numbers in input_str.
2-len(match.group(0)) gives the length of this string.
3-input_str[:-len(match.group(0))] slices the original string to remove the matched portion. It takes a slice from the beginning of input_str up to (but not including) the length of the matched string. This effectively removes the matched portion from the end of the string.
match.group(0) always returns the entire matching string, regardless of whether you used capturing groups in the regular expression or not. In this specific code snippet, match.group(0) will return the matched substring of input_str that matches the pattern (\d+),(\d+)$, which is the last two comma-separated numbers in input_str.
"""

import re

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# input string
input_str = "@twitteruser: On now - @Fusion scores first points #FirstFinals @overwatchleague @umich @umsi Michigan Athletics made out of emojis. #GoBlue,3,0"

# extract the two numbers at the end of the string
match = re.search(r'(\d+),(\d+)$', input_str)
num1 = int(match.group(1))
num2 = int(match.group(2))

# remove the two numbers from the input string
input_str = input_str[:-len(match.group(0))]

# remove punctuation from the input string
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
for i in range(len(punctuation_chars)):
    input_str = input_str.replace(punctuation_chars[i], "")

# convert the input string to lowercase and split it into a list of words
words = input_str.lower().split()

# count the number of positive and negative words in the list
pos_count = 0
neg_count = 0
for word in words:
    if word in positive_words:
        pos_count += 1
    elif word in negative_words:
        neg_count += 1

# print the results
print("Positive words:", pos_count)
print("Negative words:", neg_count)
print("Number 1:", num1)
print("Number 2:", num2)

import csv
import re
# remove punctuation from the input string
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (str1):
    for i in range (9):
        str1 = str1.replace(punctuation_chars[i], "")
    strip_punctuation = str1
    return strip_punctuation

# list of negative words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(str2):
    global neg_count
    neg_count = 0
    str2 = str2.lower()
    words = strip_punctuation(str2).split()
    for word in words:
        if word in negative_words :
            neg_count += 1
    return neg_count
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(str2):
    global pos_count
    pos_count = 0
    str2 = str2.lower()
    words = strip_punctuation(str2).split()
    for word in words:
        if word in positive_words:
            pos_count += 1
    return pos_count     
with open("project_twitter_data.csv", "r") as input_file, open("resulting_data.csv", "w", newline='') as output_file:
    # create a csv reader and writer
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    # write the header row for the output file
    writer.writerow(["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"])

    # iterate over each row in the input file
    retweet_count = []
    reply_count = []
    neg_count_list = []
    pos_count_list = []
    Net_score_list = []
    for row in reader:
        if reader.line_num == 1:  # skip header row
          continue
        num1 = row[1]
        retweet_count.append(num1)
        num2 = row[2]
        reply_count.append(num2)
        neg_count = get_neg(row[0])
        neg_count_list.append(neg_count)
        pos_count = get_pos(row[0])
        pos_count_list.append(pos_count)
        Net_Score = pos_count - neg_count
        Net_score_list.append(Net_Score)

    # delete the first item from retweet_count and reply_count lists
    retweet_count = retweet_count[1:]
    reply_count = reply_count[1:]

    # write the data rows to the output file

    for i in range(len(retweet_count)):
      writer.writerow([retweet_count[i], reply_count[i], pos_count_list[i], neg_count_list[i], Net_score_list[i]])

    


    print("net", Net_score_list)
    print(neg_count_list)
    print(pos_count_list)

"""The same project without using csv module """

# remove punctuation from the input string
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation (str1):
    for i in range (9):
        str1 = str1.replace(punctuation_chars[i], "")
    strip_punctuation = str1
    return strip_punctuation

# list of negative words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# open input and output files
input_file = open("project_twitter_data.csv", "r")
output_file = open("resulting_data.csv", "w")

# write the header row for the output file
output_file.write("Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n")

# iterate over each row in the input file
for line in input_file:
    # skip the header row
    if "retweet_count" in line:
        continue

    # extract the fields from the input row
    fields = line.strip().split(",")

    # extract the retweet and reply counts
    retweet_count = int(fields[1])
    reply_count = int(fields[2])

    # extract the tweet text and compute positive and negative scores
    tweet_text = fields[0]
    tweet_text = tweet_text.lower()
    tweet_text = strip_punctuation(tweet_text)
    words = tweet_text.split()
    pos_count = 0
    neg_count = 0
    for word in words:
        if word in positive_words:
            pos_count += 1
        elif word in negative_words:
            neg_count += 1

    # compute the net score
    net_score = pos_count - neg_count

    # write the output row to the output file
    output_file.write(f"{retweet_count},{reply_count},{pos_count},{neg_count},{net_score}\n")

# close input and output files
input_file.close()
output_file.close()