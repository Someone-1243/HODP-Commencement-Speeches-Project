import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import csv
import os
import numpy as np
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

keyword_file = "Key Phrase Data/key"
file_end = ".txt"

page = requests.get("https://en.wikipedia.org/wiki/Timeline_of_the_21st_century#2001")

soup = BeautifulSoup(page.text,'html.parser')
lists = soup.find_all('ul')

whole_text = ''
for list in lists[8:27]:
    for item in list:
        remove = False
        text = str (item)
        out = ""
        text = text[4:len(text)-4]
        length = len(text)-1
        for c in range(length, -1, -1):
            if text[c: c+1] == '>':
                remove = True

            if text[c:c+1] == '<':
                remove = False

            if not remove:
                if not text[c:c+1] == '<':
                    out = out + (text[c:c+1])

        out = out[::-1]
        whole_text = whole_text + " " + out

whole_text = whole_text.lower()

found = []

for year in range(2000, 2020):
    if year == 2001:
        continue
    if year == 2003:
        continue

    input = [year]
    flagged = []
    count = 0
    filename = keyword_file + str(year) + file_end
    f = open(filename, "r")
    lines = f.readlines()

    for word in range(len(lines)):
        lines[word] = lines[word][0: len(lines[word])-1]

    for word in lines:
        if word.lower() in whole_text:
            flagged.append(word)
            count = count + 1

    input.append(flagged)
    input.append(count / len(lines))
    found.append(input)

df = pd.DataFrame(found, columns =['Year','Words','Percentage of Keywords'])
df.to_csv ('export.csv', index = False, header=True)
print(df)
