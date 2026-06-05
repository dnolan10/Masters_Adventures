# DSC 510
# Week 8
# Programming Assignment 8.1
# Author Doug Nolan
# November 2, 2025

#import string library
import string
import os
from logging import exception


def process_line(line, word_count_dict):
    # process the line to get lowercase words and add to the dictionary
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        # ignore the '--' in the file
        if word != '--':
            word = word.lower()
            word = word.strip()
            # get all punctuation
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)


def add_word(word, word_count_dict):
    # update the word frequency: word is the key, frequency is the value
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# def pretty_print(word_count_dict):
#     # print nicely the highest to lowest frequency of words
#     value_key_list = []
#     for key, val in word_count_dict.items():
#         value_key_list.append((val,key))
#     # sort method on list's first element, the frequency
#     # reverse to get largest count first
#     value_key_list.sort(reverse=True)
#     print(f"{'Word':<15} {'Count':<15}")
#     print('-' * 21)
#     for val, key in value_key_list:
#         print(f"{key:<15} {val:<15}")

def process_file(word_count_dict, output_filename):
    # write the highest to lowest frequency of words
    try:
        with open(output_filename, 'a') as outfile:
            outfile.write(f"{'Word':<15} {'Count':<15}")
            outfile.write(' ' * 30 + '\n')

            # sort the words
            value_key_list = [(val, key) for key, val in word_count_dict.items()]
            value_key_list.sort(reverse=True)
            for key, val in sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True):
                outfile.write(f"{key:<15}{val:<15}\n")


    except Exception as e:
        print(f"Error writing to file {output_filename}: {e}")
        return None



def main():
    # define input file and get user input for the output file
    input_filename = "gettysburg.txt"
    output_filename = input("Enter the name of the output file to create:").lower().strip()
    word_count_dict = {}

    #read and process the input file
    try:
        with open(input_filename, 'r') as fileHandle:
            for line in fileHandle:
                process_line(line, word_count_dict)
    except FileNotFoundError as e:
        print(f"Error: The file was not found")
        return
    except Exception as e:
        print(e)
        return

    try:
        # write the dictionary length to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write("Gettysburg Address Word Count Report\n")
            outfile.write("------------------------------------\n")
            outfile.write(f"Length of the dictionary: {len(word_count_dict)}\n")

        process_file(word_count_dict, output_filename)

        print(f"\nReport successfully written to '{output_filename}'.")
    except Exception as e:
        print(f"Error writing report to '{output_filename}': {e}")



if __name__ == "__main__":
    main()