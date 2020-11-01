import csv
import collections

d = dict()

text = open('cleaned_repeats.csv', "r")
with open('export_dataframe.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in reader:
        for word in row:
            word = word.strip()
            word = word.lower()

            # Check if the word is already in dictionary
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

sort_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
sort_d = collections.OrderedDict(sort_list)

with open("wikirepeats.csv", 'w', newline='') as csvfile:
    fieldnames = ['phrase', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for phrase in sort_d:
        if sort_d[phrase] > 3:
            writer.writerow({'phrase': phrase, 'count': sort_d[phrase]})
