# Stylometric-Analyzer
Stylometric Analyzer is a platform which analyzes 2 authors, Shakespeare and Marlowe. Total 6 books are analyzed.

  1. Implementation of tasks

      1.1	Task-1: Setting up the preprocessor

      In this task, the preprocessor accepts the input and tokenizes in word, punctuation and single character list. 

      1.2	Task-2: Building character analyzer class

      In this task, the tokenized list (from task 1) is fed into as input and the output will consist of the frequency of individual           characters. The output is stored in a readable format using pandas data frame. 

      1.3	Task-3: Building a class for analyzing words

      This task performs the frequency analysis on a given tokenized list at the word level, extracts the stop word frequency and             word length frequency of files. The output is stored as pandas data frame.

      1.4	Task-4: Building a class for visualizing the analysis

      In this task, each individual statistic (character, punctuation, stop-word and word length) is displayed using plots in a               vertical way, and in stacked format so that user can understand the graph in a simple manner. The output images are stored             in a png format

      1.5	Task-5: Main method

      In this task, objects for each classes are created and called appropriately. A function to convert normal df into relative df           is present. A method performs required processing of data and return the relative frequency of individual statistic in a data           frame. Also, a method is used to call required visualization. In the end, steps are taken to read the input files and the               output (statistics of all required parameters) is saved in a single text file. Exceptions are implemented to catch any.

  2. Output screenshot

When the main file is run, the statistic data and visualizations are automatically displayed and stored in required directory. Refer the folders for output

  3. How to run program:

      3.1          Run the main file (%run main)
      3.2          After few min, the statistic and all 4 graphs are displayed
      3.3          The statistics is stored as text file in the directory
      3.4          And the images are saved in png format.

