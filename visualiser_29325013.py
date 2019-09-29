# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 13 May 2018
# Last Modified Date: 27 May 2018
# This code will plot the graphs for different types of frequencies of
# characters, punctuations, stopwords and word lengths for the six input
# text sequences.

import matplotlib.pyplot as plt


class AnalysisVisualiser:
    def __init__(self, all_text_stats):
        # object constructor
        self.all_texts_dataframe = all_text_stats

    def visualise_character_frequency(self):
        # the list of labels in the graph
        file_list = ["Edward_II_Marlowe.tok",
                     "Hamlet_Shakespeare.tok",
                     "Henry_VI_Part1_Shakespeare.tok",
                     "Henry_VI_Part2_Shakespeare.tok",
                     "Jew_of_Malta_Marlowe.tok",
                     "Richard_II_Shakespeare.tok"]
        # filtering the data on the basis of the key value = 'character'
        df = self.all_texts_dataframe.loc['character'][0:]
        df = df.set_index('item')[file_list]
        df.plot(title="Characters Frequency", kind='bar', figsize=(15, 7))
        # resetting the index and plotting the graphs

        df = df.sort_values('Edward_II_Marlowe.tok', ascending=False)
        # finding the characters with top frequencies in "Edward_II_Marlowe.tok"
        # and plotting the graph
        df.head(10).plot(title="Characters with Top Frequencies",
                         kind='bar',
                         figsize=(13, 7), width=0.5)

        plt.xlabel('Character')
        plt.ylabel('Frequency')
        plt.show()

    def visualise_punctuation_frequency(self):
        # the list of labels in the graph
        file_list = ["Edward_II_Marlowe.tok",
                     "Hamlet_Shakespeare.tok",
                     "Henry_VI_Part1_Shakespeare.tok",
                     "Henry_VI_Part2_Shakespeare.tok",
                     "Jew_of_Malta_Marlowe.tok",
                     "Richard_II_Shakespeare.tok"
                     ]
        # filtering the data on the basis of the key value = 'punctuation'
        df = self.all_texts_dataframe.loc['punctuation'][0:]
        df = df.set_index('item')[file_list]
        df.plot(title="Punctuation Frequency", kind='bar', figsize=(15, 7))
        # resetting the index and plotting the graphs

        df = df.sort_values('Edward_II_Marlowe.tok', ascending=False)
        # finding punctuations with top frequencies in "Edward_II_Marlowe.tok"
        # and plotting the graph
        df.head(10).plot(title="Punctuation with Top Frequencies",
                         kind='bar',
                         figsize=(13, 7), width=0.5)

        plt.xlabel('Punctuation')
        plt.ylabel('Frequency')
        plt.show()

    def visualise_stopword_frequency(self):
        # the list of labels in the graph
        file_list = ["Edward_II_Marlowe.tok",
                     "Hamlet_Shakespeare.tok",
                     "Henry_VI_Part1_Shakespeare.tok",
                     "Henry_VI_Part2_Shakespeare.tok",
                     "Jew_of_Malta_Marlowe.tok",
                     "Richard_II_Shakespeare.tok"
                     ]
        # filtering the data on the basis of the key value = 'stopword'
        df = self.all_texts_dataframe.loc['stopword'][0:]
        df = df.set_index('item')[file_list]
        df.plot(title="Stop Word Frequency", kind='bar', figsize=(15, 7))
        # resetting the index and plotting the graphs

        df = df.sort_values('Edward_II_Marlowe.tok', ascending=False)
        # finding the stop words with top frequencies in "Edward_II_Marlowe.tok"
        # and plotting the graph
        df.head(10).plot(title="Stop Word with Top Frequencies",
                         kind='bar',
                         figsize=(13, 7), width=0.5)

        plt.xlabel('Stop Word')
        plt.ylabel('Frequency')
        plt.show()

    def visualise_word_length_frequency(self):
        # the list of labels in the graph
        file_list = ["Edward_II_Marlowe.tok",
                     "Hamlet_Shakespeare.tok",
                     "Henry_VI_Part1_Shakespeare.tok",
                     "Henry_VI_Part2_Shakespeare.tok",
                     "Jew_of_Malta_Marlowe.tok",
                     "Richard_II_Shakespeare.tok"
                     ]
        # filtering the data on the basis of the key value = 'length'
        df = self.all_texts_dataframe.loc['length'][0:]
        df = df.set_index('item')[file_list]
        df.plot(title="Word Length Frequency", kind='bar', figsize=(15, 7))
        # resetting the index and plotting the graphs

        df = df.sort_values('Edward_II_Marlowe.tok', ascending=False)
        # finding word length with top frequencies in "Edward_II_Marlowe.tok"
        # and plotting the graph
        df.head(10).plot(title="Word Length with Top Frequencies",
                         kind='bar',
                         figsize=(13, 7), width=0.5)

        plt.xlabel('Length')
        plt.ylabel('Frequency')
        plt.show()
