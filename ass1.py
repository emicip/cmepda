import string
import argparse
import numpy as np
from matplotlib import pyplot as plt

def count(file_path):
    """ Program that prints the relative frequence of each letter
        of the alphabet (without distinguishing between lower and upper case) in the
        book. """
    with open(file_path) as inputFile:
        book = inputFile.read()
    book = book.lower()
    strin=string.ascii_lowercase
    my_dic=dict.fromkeys(strin,0)
    for letter in book:
        if letter in my_dic.keys():
            my_dic[letter]+=1
    SUM = sum(my_dic.values())
    for letter in my_dic.keys():
        my_dic[letter]/=SUM
    return my_dic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of the program')
    parser.add_argument("path", help="Path of the book")
    arg = parser.parse_args()
    dictionary = (count(arg.path))
    print(dictionary)

    strin=string.ascii_lowercase
    x = np.linspace(0, 25, 26)
    plt.bar(dictionary.keys(), dictionary.values())
    plt.show()
