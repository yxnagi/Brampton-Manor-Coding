from validation import *
import csv

itemslist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def final():
    pass

def askinteger():
    pwnumber = validate_int(message="PLEASE ENTER AN INTEGER BETWEEN 1 AND 1000000000 ",
                            minimum=1,
                            maximum=1000000000)
    return pwnumber

def check_if_generated():
    with open ('passwords.txt', 'r+') as pwcsv:
        pwcsv.write('[1,2,3,4,5]')

if __name__ == "__main__":
    check_if_generated()
    final()
