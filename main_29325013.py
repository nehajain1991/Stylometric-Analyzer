# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 13 May 2018
# Last Modified Date: 27 May 2018
# This code is the main code where all the functions to analyse the frequencies
# and visualise them will be called for the six input text sequences.

import pandas as pd
from word_29325013 import WordAnalyser
from character_29325013 import CharacterAnalyser
from preprocessor_29325013 import Preprocessor
from visualiser_29325013 import AnalysisVisualiser


def read_input(file_name):
    # function to read the input files and pass them to the other functions.
    # It will throw exceptions if any encountered.
    try:  # this try catch will catch any exception if the file does not exists.
        file_handle = open(file_name, 'r')

        if not file_handle.read(1):
           file_handle.close()
           raise Exception("file_name")

    except IOError:
        print("File", file_name,
              "does not exists, Please place the file on the location")
        return None

    except Exception as message:
        print(message, "has no input text in it")
        return None

    else:  # otherwise it will read the file and return it as the string.
        file_handle = open(file_name, 'r')
        input_sequence = ''
        for line in file_handle:
            input_sequence += line
        print(input_sequence)
        return input_sequence


def character_frequency(file_list):
    # this function is called to calculate the character level frequencies.
    list_completed = []
    for each in file_list:
        input_sequence = read_input(each)
        if input_sequence is not None:  # if the file exists
            file1 = Preprocessor()  # preprocess the file to tokenised list
            char = CharacterAnalyser()  # defined object of CharacterAnalyser
            file1.tokensise(input_sequence)
            char.analyse_characters(file1.get_tokenised_list())
            # passed the tokenised list to calculate character level frequencies

            all_dataframe = char.character_dataframe
            # stored the character frequency to a variable

            # merged all the frequencies of all the files to one dataframe
            if len(list_completed) == 0:
                all_dataframe.columns = ["item", each]
                list_completed.append(each)
                new_dataframe = all_dataframe
            else:
                all_dataframe.columns = ["item", each]
                new_dataframe = new_dataframe.merge(all_dataframe, on="item",
                                                    how="outer")

        else:  # if file does not exist, exit the code.
            return None

    new_dataframe = pd.concat([new_dataframe], keys=['character'])
    return new_dataframe


def punctuation_frequency(file_list):
    # this function is called to calculate the punctuation frequencies.
    list_completed = []
    for each in file_list:
        input_sequence = read_input(each)
        if input_sequence is not None:  # if the file exists
            file1 = Preprocessor()  # preprocess the file to tokenised list
            char = CharacterAnalyser()  # defined object of CharacterAnalyser
            file1.tokensise(input_sequence)
            char.analyse_characters(file1.get_tokenised_list())
            # passed the tokenised list to calculate punctuation frequencies
            punctuation_frequency_datafarame = char.get_punctuation_frequency()
            # calculate punctuation frequency

            all_dataframe = punctuation_frequency_datafarame
            # stored the punctuation frequency to a variable

            # merged all the frequencies of all the files to one dataframe
            if len(list_completed) == 0:
                all_dataframe.columns = ["item", each]
                list_completed.append(each)
                new_dataframe = all_dataframe

            else:

                all_dataframe.columns = ["item", each]
                new_dataframe = new_dataframe.merge(all_dataframe, on="item",
                                                    how="outer")

        else:  # if file does not exist, exit the code.
            return None

    new_dataframe = pd.concat([new_dataframe], keys=['punctuation'])
    return new_dataframe


def stopword_frequency(file_list):
    # this function is called to calculate the stop word frequencies.
    list_completed = []
    for each in file_list:
        input_sequence = read_input(each)
        if input_sequence is not None:  # if the file exists
            file1 = Preprocessor()  # preprocess the file to tokenised list
            word = WordAnalyser()  # defined object of WordAnalyser
            file1.tokensise(input_sequence)
            word.analyse_words(file1.get_tokenised_list())
            # passed the tokenised list to calculate word level frequencies

            stopword_frequency_dataframe = word.get_stopword_frequency()
            # calculate stopword frequency

            if stopword_frequency_dataframe is not None:
                # if there is no error with the stop word file
                all_dataframe = stopword_frequency_dataframe
                # stored the stop word frequency to a variable

                # merged all the frequencies of all the files to one dataframe
                if len(list_completed) == 0:
                    all_dataframe.columns = ["item", each]
                    list_completed.append(each)
                    new_dataframe = all_dataframe

                else:

                    all_dataframe.columns = ["item", each]
                    new_dataframe = new_dataframe.merge(all_dataframe,
                                                        on="item",
                                                        how="outer")
            else: # if file does not exist, exit the code.
                return None
        else: # if file does not exist, exit the code.
            return None

    new_dataframe = new_dataframe.sort_values('item')
    new_dataframe = pd.concat([new_dataframe], keys=['stopword'])

    return new_dataframe


def length_frequency(file_list):
    # this function is called to calculate the word length frequencies.
    list_completed = []
    for each in file_list:
        input_sequence = read_input(each)
        if input_sequence is not None:   # if the file exists
            file1 = Preprocessor()  # preprocess the file to tokenised list
            word = WordAnalyser()  # defined object of WordAnalyser
            file1.tokensise(input_sequence)
            word.analyse_words(file1.get_tokenised_list())
            # passed the tokenised list to calculate character level frequencies
            length_frequency_datfarame = word.get_word_length_frequency()
            # calculate word length frequency

            all_dataframe = length_frequency_datfarame
            # stored the word length frequency to a variable

            # merged all the frequencies of all the files to one dataframe
            if len(list_completed) == 0:
                all_dataframe.columns = ["item", each]
                list_completed.append(each)
                new_dataframe = all_dataframe

            else:

                all_dataframe.columns = ["item", each]
                new_dataframe = new_dataframe.merge(all_dataframe, on="item",
                                                    how="outer")
        else:   # if file does not exist, exit the code.
            return None

    new_dataframe = pd.concat([new_dataframe], keys=['length'])

    return new_dataframe


def main():
    # file list to hold the names of all six input texts
    file_list = ['Edward_II_Marlowe.tok',
                 'Hamlet_Shakespeare.tok',
                 'Henry_VI_Part1_Shakespeare.tok',
                 'Henry_VI_Part2_Shakespeare.tok',
                 'Jew_of_Malta_Marlowe.tok',
                 'Richard_II_Shakespeare.tok'
                  ]

    print("The comparison will be done on the below input texts:")
    print('1. Edward_II_Marlowe.tok\n'
          '2. Hamlet_Shakespeare.tok\n'
          '3. Henry_VI_Part1_Shakespeare.tok\n'
          '4. Henry_VI_Part2_Shakespeare.tok\n'
          '5. Jew_of_Malta_Marlowe.tok\n'
          '6. Richard_II_Shakespeare.tok')
    # Menu to choose the frequency to analyse, depending upon option,
    # frequency will be calculated and graph will be plotted.

    # The calculated frequencies will be stored in a file named "All.csv" where
    # all the statistics can be viewed.
    continue_exit = 'Y'
    while continue_exit in ('Y', 'y'):
        option = input("Please input the type of comparison you want to perform:\n"
                       "1. Character\n"
                       "2. Punctuation\n"
                       "3. Stopword\n"
                       "4. Word length\n"
                       "5. All")

        if option == '1':
            new_dataframe = character_frequency(file_list)

            if new_dataframe is not None:
                new_dataframe.to_csv('All.csv')
                analysis = AnalysisVisualiser(new_dataframe)
                analysis.visualise_character_frequency()

        elif option == '2':
            new_dataframe = punctuation_frequency(file_list)

            if new_dataframe is not None:
                new_dataframe.to_csv('All.csv')
                analysis = AnalysisVisualiser(new_dataframe)
                analysis.visualise_punctuation_frequency()

        elif option == '3':
            new_dataframe = stopword_frequency(file_list)

            if new_dataframe is not None:
                new_dataframe.to_csv('All.csv')
                analysis = AnalysisVisualiser(new_dataframe)
                analysis.visualise_stopword_frequency()

        elif option == '4':
            new_dataframe = length_frequency(file_list)

            if new_dataframe is not None:
                new_dataframe.to_csv('All.csv')
                analysis = AnalysisVisualiser(new_dataframe)
                analysis.visualise_word_length_frequency()

        elif option == '5':
            character = character_frequency(file_list)
            if character is not None:
                puntuation = punctuation_frequency(file_list)
                stopword = stopword_frequency(file_list)
                word_length = length_frequency(file_list)

                if stopword is not None:
                    new_dataframe = pd.concat(
                        [character, puntuation, stopword, word_length])
                    new_dataframe.to_csv('All.csv')
                    analysis = AnalysisVisualiser(new_dataframe)
                    analysis.visualise_character_frequency()
                    analysis.visualise_punctuation_frequency()
                    analysis.visualise_stopword_frequency()
                    analysis.visualise_word_length_frequency()

                else:
                    print("The stop word frequency is not calculated as there "
                          "was an error in the stop word URL")
                    new_dataframe = pd.concat(
                        [character, puntuation, word_length])
                    new_dataframe.to_csv('All.csv')
                    analysis = AnalysisVisualiser(new_dataframe)
                    analysis.visualise_character_frequency()
                    analysis.visualise_punctuation_frequency()
                    analysis.visualise_word_length_frequency()

        else:
            print("Invalid Option")

        continue_exit = input("Do you want to analyse more?, Press Y or y")


if __name__ == "__main__":
    main()
