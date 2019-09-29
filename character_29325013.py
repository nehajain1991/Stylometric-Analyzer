# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 13 May 2018
# Last Modified Date: 27 May 2018
# This code will analyse the frequencies of characters and punctuations
# in the six input text sequences.


import pandas as pd

class CharacterAnalyser:
    def __init__(self):
        # object constructor
        self.character_dataframe = pd.DataFrame(
            columns=['item', 'frequency'])

    def __str__(self):
        # print the dataframe
        print_string = 'Frequency each character is \ncharacter   Frequency\n '
        for index, row in self.character_dataframe.iterrows():
            entry = row['item'] + '              ' + str(row['frequency'])
            print_string += (entry + '\n')
        return print_string

    def analyse_characters(self, tokenised_list):
        list_new = []

        # this will form a list of characters with stripping off the blanks and
        # new line form the tokenised list
        for each in tokenised_list:
            for character in each:
                if character != '' and character != '\n':
                    list_new.append(character)
        list_new.sort() # sort the list

        # assign list to one column of the datafarame
        self.character_dataframe['item'] = list_new
        self.character_dataframe['frequency'] = \
            self.character_dataframe.groupby('item')['item'].transform('count')
        # count the frequency of the characters in the list
        self.character_dataframe['frequency'] = \
            self.character_dataframe['frequency']/len(list_new)
        # calculate the relative frequency
        self.character_dataframe = \
            self.character_dataframe.drop_duplicates(keep='first')
        # drop the duplicates

    def get_punctuation_frequency(self):
        # punctuation dataframe
        punctuation_dataframe = pd.DataFrame(
            columns=['item', 'frequency'])
        for index, row in self.character_dataframe.iterrows():
            if not row['item'].isalpha() and not row['item'].isdigit():
                # check if the item is punctaution
                entry = [row['item'], row['frequency']]
                punctuation_dataframe.loc[len(punctuation_dataframe)] = entry
                # assign the values to the new dataframe
        return punctuation_dataframe
