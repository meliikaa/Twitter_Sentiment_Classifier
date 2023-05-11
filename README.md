# Twitter_Sentiment_Classifier
Sentiment Classifier Project

This repository contains code for a sentiment classifier, which analyzes a CSV file of tweets, determines their overall sentiment, and make a graph out of it in an excel file. The repository contains several Python scripts that walk through the project step-by-step, as well as a final script that combines all of the functionality into a single script.
Overview

The sentiment classifier works by analyzing each tweet in the CSV file and scoring it based on the number of positive and negative words it contains. The positive and negative words are contained in separate text files that are read in by the program.

The final output is a new CSV file that contains columns for the number of retweets and the number of replies as well as the positive score, negative score, and net score (positive score minus negative score).

Project Structure

The repository contains several Python scripts that walk through the project step-by-step:

    step1: Cleans the original tweet data by removing any extraneous characters or punctuation.
    step2: Analyzes the sentiment of each tweet by scoring it based on the number of positive and negative words it contains.
    step3: Extracts the number of retweets and replies from each tweet.
    step4: Combines all of the previous functionality into a single script and writes the final output CSV file.

The repository also contains a final script, sentiment_classifier.py, that combines all of the functionality into a single script.
How to Use

To use the sentiment classifier, follow these steps:

    Clone the repository to your local machine.
    Install any necessary dependencies (e.g. numpy, pandas).
    Run the sentiment_classifier.py script, which combines all of the functionality into a single script.
    The final output file, resulting_data.csv, will be generated in the same directory as the script.
    Lastly, you can open the file in excel or google sheet to make a graph out of the datas.


The sentiment classifier is a useful tool for analyzing large datasets of tweets and determining their overall sentiment. The code in this repository provides a step-by-step guide to building a sentiment classifier from scratch, as well as a final script that combines all of the functionality into a single script.
This repository also contains some other weekly codes that can help you gain an understanding of the logic behind the code, as they guide you through each step in the process of learning the syntax of the code.
(This project is based on a course on Python offered by Michigan University.)
