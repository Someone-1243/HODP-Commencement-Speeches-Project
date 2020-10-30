import csv
import collections
  
d = dict() 
  
for year in range(2000, 2020):
    speech_filename = "key" + str(year) + ".txt"
    text = open(speech_filename, "r")

    for line in text: 
        line = line.strip() 
        line = line.lower() 

        # Check if the word is already in dictionary 
        if line in d: 
            d[line] = d[line] + 1
        else: 
            d[line] = 1

sort_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
sort_d = collections.OrderedDict(sort_list)

with open("repeats.csv", 'w', newline='') as csvfile:
    csvfile.write("hi")
    fieldnames = ['phrase', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for phrase in sort_d:
        if sort_d[phrase] > 3:
            writer.writerow({'phrase': phrase, 'count': sort_d[phrase]})
