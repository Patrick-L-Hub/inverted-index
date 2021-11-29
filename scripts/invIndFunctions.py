import os
import re
import pdb
import string


def find_text_files():
    '''
    This is to get txt files from the Text_files folder in the directory
    that the program is currently running in.
    '''

    dir_path = os.path.dirname('Text_files/')
    filelist = list()
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.txt'):
                filelist.append((file,root+'\\'+file))
    return filelist


def findWords(text_line):
    '''
    The function findWords is given one line from a text file and parses through
    every character searching for special characters.  If one is found the
    special character is removed, then the function stores each word as an element in
    a list to be returned
    '''

    wordlist =[]
    line = text_line.split(" ")
    #print("THE LINE ISSSSSSSSSS"+text_line)
    for x in line:
        word =''
        index = 0
        while index in range(len(x)):
            try:
                if x[index] == '\\'and x[index+1] in string.ascii_letters:
                    index += 2
                    continue
            except IndexError:
                pass
            #The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers)
            if x[index].isalnum():
                word += x[index]
            index += 1
        if word.isalnum():
            wordlist.append(word)
    return wordlist


def wordSearch(invIndex, filelist):
    '''
    The function takes in the users input word, checks if it is a key in the
    inverted index dictionary and either calls another function to get the
    locations or tells the user that the word was not found in the given
    text files
    '''
    word = input("Search for a word:\n")
    if word in invIndex:
        print("\nSyntax for word location is (file: [line number, word number]):\n")
        printResults(invIndex, word)
    elif word not in invIndex:
        print('Word not found.')


def printResults(invIndex, word):
    '''
    The function disects the value associated with invIndex[word], grabing
    the file names and line numbers/word numbers telling the locations of the
    word that match the provided key. In doing so it creates a  dictionary
    for each file that has the locations of the word for that text file
    '''
    fileset = set()
    logfile = dict()
    for file in invIndex[word]:
        fileset.add(file[0])
    for file in fileset:
        logfile[file] = []
    for val in invIndex[word]:
        filename = val[0]
        if filename in logfile:
            logfile[filename].append((val[1],val[2]))
    for x in logfile.keys():
        print(x, ":" ,logfile[x])
