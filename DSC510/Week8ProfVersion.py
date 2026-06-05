# This file is a working copy of the week 8 (12 week program)
# gettysburg processing or the week 7 (10 week program)

#import string library
import string


def process_line(line, word_count_dict):

    """Process the line to get lowercase words to add to the dictionary. """
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        # ignore the '−−' that is in the file
        if word != '--':
            word = word.lower()
            word = word.strip()
            # get commas, periods, and other punctuation out as well
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)


def add_word(word, word_count_dict):

    """Update the word frequency: word is the key, frequency is the value """
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

'''
def pretty_print(word_count_dict):
    # This is how to print the dictionary in reverse sorted order using the format() method
    """Print nicely from highest to lowest frequency """
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    # sort method sorts on list's first element, the frequency.
    # Reverse to get biggest first
    value_key_list.sort(reverse=True)
    # value_key_list = sorted([v,k) for k, v in value_key_list.items()]
    print(f"{'Word':<15} {'Count':<15}")
    print(' ' * 21)
    for val, key in value_key_list:
        print(f"{key:<15} {val:<15}")
        '''

def process_file(word_count_dict, output_filename):
    # This is how to print the dictionary in reverse sorted order using the format() method
    """Print nicely from highest to lowest frequency """
    value_key_list = []
    word_count_dict = {}

    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    # sort method sorts on list's first element, the frequency.
    # Reverse to get biggest first
    value_key_list.sort(reverse=True)
    # value_key_list = sorted([v,k) for k, v in value_key_list.items()]
    with open("gettysburg.txt", 'r') as fileHandle:
        with open(output_filename, 'a') as outfile:
            for val, key in value_key_list:
                outfile.write(value_key_list)



def main():
    word_count_dict = {}
    output_filename = input("Please enter the file name to output:").lower().strip()

    process_file = process_line(output_filename)
    try:
        with open("gettysburg.txt", 'r') as fileHandle:
            for line in fileHandle:
                process_line(line, word_count_dict)
        # data = fileHandle.read()
    except FileNotFoundError as e:
        print(e)

    print('Length of the dictionary:', len(word_count_dict))
    process_file(word_count_dict, output_filename)


if __name__ == "__main__":
    # execute only if run as a script
    main()
