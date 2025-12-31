import csv
import json
from fileanalyzer import analyzer,make_dictlist


csvfile=None
#filename,total_words,unique_words,avg_word_length

paths=["files/file1.txt","files/file2.txt","files/file3.txt","files/file4.txt"]



'''
with open(fpath,mode='r') as file:
    txfile=file.read()
    print(txfile)
    csvfile=csv.reader(file)
    for line in csvfile:
        print(line[1])'''


'''
print("word count:",analyzer.countWord(fpath))
print("numb count:",analyzer.countNumbs(fpath))
print("unique words count:",analyzer.uniqueWcount(fpath))'''

alldicts=make_dictlist(paths)
print("rows:",alldicts)
print("filese in convertion process:",paths)
input("press Enter to convert ...")


with open('allfileslog.csv','w',newline='') as csvfile:
    fields=alldicts[0].keys()
    writer=csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(alldicts)
