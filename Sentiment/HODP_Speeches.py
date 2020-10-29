import requests
from pprint import pprint
import csv
import helper
import os

speech_file = "Commencement Speeches/Commencement Speeches/"
txt_end = ".txt"
file_start = "sentiments"
file_end = ".csv"

subscription_key = ""
endpoint = ""
sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"

for year in range(2006, 2007):
    speech_filename = speech_file + str(year) + txt_end
    export_file = file_start + str(year) + file_end

    f = open(speech_filename, "r", encoding="utf8", errors='ignore')
    whole_text = f.read()
    print(whole_text)
    text = helper.chunk(whole_text)

    pprint(text)

    sentiments_list = []
    for index in range(len(text)):
        documents = text[index]

        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_url, headers=headers, json=documents)
        sentiments = response.json()

        pprint(sentiments)
        sentiments_list.append(sentiments)
    print ('---------------------------------------------------------------------------------------------------------')

    with open(export_file, 'w', newline='',  encoding="utf8", errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        counter = 0
        writer.writerow(['id','sentiment','positiveScore', 'neutralScore', 'negativeScore', 'text'])
        for sentiments in sentiments_list:
            for doc in sentiments['documents']:
                #for item in doc:
                li = []
                pprint(doc)
                li.append(doc['id'])
                li.append(doc['sentiment'])
                li.append(doc['confidenceScores']['positive'])
                li.append(doc['confidenceScores']['neutral'])
                li.append(doc['confidenceScores']['negative'])
                for i in range(len(doc['sentences'])):
                    li.append(doc['sentences'][i]['text'])
                writer.writerow(li)
        f.close()
