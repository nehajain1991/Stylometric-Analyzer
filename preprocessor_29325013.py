# Author: Neha Jain
# Student_ID: 29325013
# Start Date: 13 May 2018
# Last Modified Date: 27 May 2018
# This code is the main code where all the functions to decode the morse code
# sequence using main() function and to analyse it will be called

class Preprocessor:

    def __init__(self):
        # object constructor
        self.token_list = []

    def __str__(self):
        # print the tokenised list
        print_string = 'The tokens in the input file is '
        for each in self.token_list:
            print_string += (each + ', ')
        return print_string

    def tokensise(self, input_sequence):
        # this will take the file text as string as input and tokenise it
        input_sequence = input_sequence.replace('\n', ' ')
        list_input = input_sequence.split(' ')
        for each in list_input:
            each = each.strip('\n').lower()
            self.token_list.append(each)

    def get_tokenised_list(self):
        # this will return the tokenised list of the input
        return self.token_list
