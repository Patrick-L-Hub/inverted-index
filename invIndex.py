
from scripts.invIndFunctions import find_text_files,findWords,wordSearch

def main():
    '''
    Inverted index script
    Given a set of files, the script creates an inverted index and
    prompts a user to search for a word or character
    using the index.  The index returns a list of files that contain
    the query term/terms.  The users search request returns the files and
    line/word numbers within the files where the word exits
    '''
    #find all .txt files in the working directory add location to filelist
    filelist = find_text_files()
    # Inverted index to be created is a dictionary where keys are words
    # and values are the file name and word locations within the files
    invIndex = dict()

    #check the words in each line to see if they are in the index if not add
    #if so store locations
    for file in filelist:
        filename = file[0]
        openfile = open(file[1], mode ='r')
        linelist = openfile.readlines()
        linenum = 0
        for line in linelist:
            linenum += 1
            wordlist = findWords(line)
            wordnum = 0
            for word in wordlist:
                wordnum += 1
                if word in invIndex:
                    invIndex[word].append((filename, linenum, wordnum))
                    continue
                else:
                    invIndex[word] = [(filename, linenum, wordnum)]

    search = 'y'
    while (search == 'y' or search == 'Y'):
        wordSearch(invIndex, filelist)
        search = input("\nWould you like to search for another word? (y/n)\n")

if __name__ == "__main__":
    main()
