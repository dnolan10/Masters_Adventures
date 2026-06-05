# DSC 510
# Week 7
# Programming Assignment 7.1
# Author Doug Nolan
# October 26, 2025


def add_word(word, word_dict):
    #add words to dictionary & update counts
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] =1

def process_line(line, word_dict):
    #remove punctuation and convert to lowercase
    for ch in '",.!?:;-_()[]{}\'"\n':
        line = line.replace(ch, " ")
    words = line.lower().split()

    for word in words:
        add_word(word, word_dict)

def pretty_print(word_dict):
    #pretty print dictionary in tabluar format sorted by count
    print(f"{'Word':<15}{'Count':>5}")
    print("-" * 30)

    for word, count in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{word:<15}{count:>5}")

def main():
    word_dict = {}
    filename = "gettysburg.txt"

    try:
        with open(filename, 'r') as fileHandle:
            for line in fileHandle:
                process_line(line, word_dict)
            print(f"\nLength of dictionary : {len(word_dict)}\n")
            pretty_print(word_dict)
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()