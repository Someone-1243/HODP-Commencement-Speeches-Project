import requests
import helper
import json
import csv
import os

url = "https://japerk-text-processing.p.rapidapi.com/sentiment/"

speech_file = "Sentiment/Commencement Speeches/Commencement Speeches/"
txt_end = "_1.txt"
file_start = "Sentiment/Second_API/csv/sentiments2_"
file_end = ".csv"


headers = {
    'content-type': "application/x-www-form-urlencoded; charset=utf-8",
    # 'x-rapidapi-key': "",
    'x-rapidapi-host': "japerk-text-processing.p.rapidapi.com"
    }

for year in range(2006, 2007):
    speech_filename = speech_file + str(year) + txt_end
    export_file = file_start + str(year) + file_end


    f = open(speech_filename, "r", encoding="utf8", errors='ignore')
    whole_text = f.read()
    print(whole_text)
    print('==========================================================================')
    print('==========================================================================')
    print('==========================================================================')
    print('==========================================================================')
    text = helper.chunk(whole_text)
    print(text)
    
    sentiments=[]

    for document in text:
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

            pos = raw_pos/sum
            neutral = raw_neutral/sum
            neg = raw_neg/sum

            sentiments.append((sentiment, raw_pos, raw_neutral, raw_neg, sum, pos, neutral, neg))

    with open(export_file, 'w', newline='',  encoding="utf8", errors='ignore') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['sentiment','raw_positiveScore', 'raw_neutralScore', 'raw_negativeScore', 'Sum', 'pos', 'neutral', 'neg'])
        for sentiment in sentiments:
            writer.writerow([sentiment[0], sentiment[1], sentiment[2], sentiment[3], sentiment[4], sentiment[5], sentiment[6], sentiment[7]])
            
    f.close()

    
#print(json.loads(response.text)['probability'])

#{"probability": {"neg": 0.64623859986492871, "neutral": 0.37411991437589281, "pos": 0.35376140013507135}, "label": "neg"}