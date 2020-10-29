key = ""
endpoint = ""


from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def key_phrase_extraction(client):

    try:
        f = open("Commencement Speeches/2020.txt", "r")
        w = open("Key Phrase Data/key2020.txt", "w")

        whole_text = f.read()
        f.close()
    
        start = 0
        end = 5000
        
        while start < end:
            try:
                index = whole_text.rindex(' ', start, end)
                end = index + 1
            except ValueError:
                end = end

            documents = [whole_text[start:end]]
            response = client.extract_key_phrases(documents = documents)[0]

            if not response.is_error:
                for phrase in response.key_phrases:
                    w.writelines([phrase,"\n"])
            else:
                print(response.id, response.error)

            start = end

            if start < len(whole_text) - 5000:
                end = start + 5000
            else:
                end = len(whole_text)

        w.close()
        
    except Exception as err:
        w.close()
        print("Encountered exception. {}".format(err))
     
key_phrase_extraction(client)
