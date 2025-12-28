import csv
import json
from fileanalyzer import analyzer

csvfile=None
#filename,total_words,unique_words,avg_word_length

fpath="files/file2.txt"

'''
with open(fpath,mode='r') as file:
    txfile=file.read()
    print(txfile)
    csvfile=csv.reader(file)
    for line in csvfile:
        print(line[1])'''
print("word count:",analyzer.countWord(fpath))
print("numb count:",analyzer.countNumbs(fpath))
print("unique words count:",analyzer.uniqueWcount(fpath))
