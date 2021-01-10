import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pprint
import csv
import helper
import os

#subscription_key = ""
#endpoint = ""
sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"

driver = webdriver.Chrome('C:\Download\chromedriver_win32\chromedriver.exe')

page = requests.get("https://en.wikipedia.org/wiki/Timeline_of_the_21st_century#2001")

soup = BeautifulSoup(page.text,'html.parser')
lists = soup.find_all('ul')

years = []
for list in lists[8:29]:
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
    text.append(helper.chunk(year))

sentiments_list = []
for index in range(len(text)):
    documents = text[index][0]
    
    headers = {"ocp-apim-subscription-key": subscription_key}
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentiments = response.json()

    pprint(sentiments)
    sentiments_list.append(sentiments)

with open ('wiki_sentiments2.csv', 'w', newline ='', encoding="utf8", errors='ignore') as csvfile:
    writer = csv.writer(csvfile)
    counter = 0
    year = 2001
    writer.writerow(['Year', 'Sentiment','Positive Score', 'Neutral Score', 'Negative Score', 'Text'])
    for sentiments in sentiments_list:
            for doc in sentiments['documents']:
                #for item in doc:
                li = []
                pprint(doc)
                li.append(year)
                li.append(doc['sentiment'])
                li.append(doc['confidenceScores']['positive'])
                li.append(doc['confidenceScores']['neutral'])
                li.append(doc['confidenceScores']['negative'])
                for i in range(len(doc['sentences'])):
                    li.append(doc['sentences'][i]['text'])
                writer.writerow(li)
                print("printed")
            
            year = year + 1

