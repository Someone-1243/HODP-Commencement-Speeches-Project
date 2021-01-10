import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import csv
import helper
import os
import json

url = "https://japerk-text-processing.p.rapidapi.com/sentiment/"

headers = {
    'content-type': "application/x-www-form-urlencoded; charset=utf-8",
    'x-rapidapi-key': "26c6528ad6mshea36b2df94b4ab9p1a8fe5jsn750c57e0ead4",
    'x-rapidapi-host': "japerk-text-processing.p.rapidapi.com"
    }

driver = webdriver.Chrome('C:\Download\chromedriver_win32\chromedriver.exe')

page = requests.get("https://en.wikipedia.org/wiki/Timeline_of_the_21st_century#2001")

soup = BeautifulSoup(page.text,'html.parser')
lists = soup.find_all('ul')

years = []
for list in lists[9:29]:
    package = ""
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
        package = package + " " + out
    years.append(package)


text = []
for year in years:
    pprint(year)
    print('===========================================')
    print('===========================================')
    print('===========================================')
    text.append(helper.chunk(year))


y = 2001

with open ('sentiment/second_api/wiki_sentiments2_averages.csv', 'w', newline ='', encoding="utf8", errors='ignore') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['year', 'pos', 'neutral', 'neg'])
    for year in text:
        count = 0
        pos = 0
        neutral = 0
        neg = 0
        for document in year:
            for item in document['documents']:
                p = item['text']
                print('------------------------------')
                print(item['text'])
                payload = "text=" + p

                response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
                r_json = json.loads(response.text)
                data=r_json['probability']
                sentiment=r_json['label']
                raw_neg=data['neg']
                raw_neutral=data['neutral']
                raw_pos=data['pos']
            
                sum = raw_neg + raw_neutral + raw_pos

                pos += raw_pos/sum
                neutral += raw_neutral/sum
                neg += raw_neg/sum

                count += 1

        pos /= count
        neutral /= count
        neg /= count

        writer.writerow([y, pos, neutral, neg])
        y+= 1
            


#with open ('Sentiment/Second_API/wiki_sentiments2.csv', 'w', newline ='', encoding="utf8", errors='ignore') as csvfile:
#    writer = csv.writer(csvfile)
#    counter = 0
#    year = 2001
#    writer.writerow(['Year', 'Sentiment','Positive Score', 'Neutral Score', 'Negative Score', 'Text'])
#    for sentiments in sentiments_list:
#            for doc in sentiments['documents']:
#                #for item in doc:
#                li = []
#                pprint(doc)
#                li.append(year)
#                li.append(doc['sentiment'])
#                li.append(doc['confidenceScores']['positive'])
#                li.append(doc['confidenceScores']['neutral'])
#                li.append(doc['confidenceScores']['negative'])
#                for i in range(len(doc['sentences'])):
#                    li.append(doc['sentences'][i]['text'])
#                writer.writerow(li)
#                print("printed")
            
#            year = year + 1

