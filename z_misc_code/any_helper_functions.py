
def containsAny(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]


def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

def containsCount(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    tally=0
    for c in set:
        if c in str: tally +=1
    return tally


def split(word):
    return [char for char in word]


# SETUP


import pathlib

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  
input = script_path / 'input.txt'  #  

file_in = input #_test


if __name__ == "__main__":

  with open(file_in, 'r') as file:
    data=[line.split() for line in file]
