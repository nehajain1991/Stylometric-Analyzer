# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 13 May 2018
# Last Modified Date: 27 May 2018
# This code will analyse the frequencies of words, stop words and different
# word lengths in the six input text sequences.


import pandas as pd
import urllib.request
import urllib.error


class WordAnalyser:
    def __init__(self):
        # object constructor
        self.word_dataframe = pd.DataFrame(
            columns=['item', 'frequency'])

    def __str__(self):
        # print the dataframe
        print_string = 'Frequency each word is \nWord  Frequency\n '
        for index, row in self.word_dataframe.iterrows():
            entry = row['item'] + '                 ' + str(row['frequency'])
            print_string += (entry + '\n')
        return print_string

    def analyse_words(self, tokenised_list):
        tokenised_list_new = []

        # this will form a list of word with stripping off the punctuation and
        # new line form the tokenised list
        for each in tokenised_list:
            if not each.isalpha() and not each.isdigit():
                if len(each)>1 and each != '\n':
                    tokenised_list_new.append(each)
            else:
                tokenised_list_new.append(each)
        tokenised_list_new.sort()  # sort the list
        self.word_dataframe["item"] = tokenised_list_new
        # assign list to one column of the datafarame
        self.word_dataframe["frequency"] = self.word_dataframe.groupby("item")[
            "item"].transform('count')
        # count the frequency of the words in the list
        self.word_dataframe["frequency"] = \
            self.word_dataframe["frequency"] / len(tokenised_list)
        # calculate the relative frequency
        self.word_dataframe = self.word_dataframe.drop_duplicates(keep='first')
        # drop the duplicates

    def get_stopword(self):
        # stopword URL
        url = 'http://www.lextek.com/manuals/onix/stopwords1.html'

        local_file = 'stop.txt'
        try:
            # retrive the contents of the URL in a file
            urllib.request.urlretrieve(url, local_file)

            file_handle = open('stop.txt', 'r')
            new_file = open("new.txt", 'w')
            # start of the stop word
            startquery = "about\n"
            # end of the stop word
            endquery = "z\n"
            lines = file_handle.readlines()

            i = 0
            while i < 1102:
                # start traversing the file for the start of the stop word and
                # keep writing it to the stopword file
                if lines[i] == startquery:
                    while lines[i] != endquery and i != 1101:
                        new_file.write(lines[i])
                        i = i + 1
                    break
                i += 1

            new_file.close()
            new_file = open("new.txt", 'r')
            file_handle = new_file.read()
            file_handle = file_handle.replace('\n\n', '\n')
            # replace extra new lines
            stopword = open('stopword.txt', 'w')

            stopword.write(file_handle)
            stopword.close()
            new_file.close()

        except (urllib.error.HTTPError, urllib.error.URLError):
            print("There is a problem in the Stop word URL")

    def get_stopword_frequency(self):
        self.get_stopword()
        # making the stopword file
        try:  # check if the file exists
            file_stopword = open('stopword.txt', 'r')

            list_of_stop_words = []
            # making the list of stop words from the file after removing any
            # extra characters.
            for line in file_stopword:
                line = line.strip('\n')
                list_of_stop_words.append(line)
            list_of_stop_words.sort()
            # stopword dataframe
            stop_dataframe = pd.DataFrame(
                columns=['item', 'frequency'])

            for index, row in self.word_dataframe.iterrows():

                word = row['item']
                word = word.strip('\n')
                word = word.strip(' ')
                if word in list_of_stop_words:
                    # check if the item is stopword
                    entry = [row['item'], row['frequency']]
                    stop_dataframe.loc[
                        len(stop_dataframe)] = entry
                    # assign the values to the new dataframe
            file_stopword.close()
            return stop_dataframe

        except IOError:  # if the file does not exist
            return None

    def get_word_length_frequency(self):
        # length dataframe
        length_dataframe = pd.DataFrame(
            columns=['item', 'length'])
        for index, row in self.word_dataframe.iterrows():
            # calculate the length of each word and store it
            word = row["item"]
            length = len(word)
            length_dataframe.loc[len(length_dataframe)] = [word, length]

        new_dataframe = self.word_dataframe.merge(length_dataframe,
                                                  on="item", how="inner")

        new_dataframe["frequency"] = \
            new_dataframe.groupby('length')["frequency"].transform('sum')
        # count the frequency of the word lengths in the list
        length_dataframe = new_dataframe
        del length_dataframe['item']
        length_dataframe.columns = ['frequency', 'item']
        length_dataframe = \
            length_dataframe.reindex(columns=['item', 'frequency'])

        # calculate the relative frequency
        length_dataframe = length_dataframe.drop_duplicates(keep='first')
        # drop the duplicates
        length_dataframe = length_dataframe.sort_values('item')
        # sorting the list
        return length_dataframe
