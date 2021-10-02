from google.cloud import language_v1
import os
import argparse
import json
import sys
import secrets
import string

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_apikey.json"

# Invokation Argument --
n = len(sys.argv)

# Checking if argument provided is correct --
if n < 2:
    print("Syntax:\t\tgoogle_nlp.py json_filename\nFor Example:\google_nlp.py apple.json")
    exit()

def entity_analysis(text_content):
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    encoding_type = language_v1.EncodingType.UTF8
    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    return_str = ""
    for entity in response.entities:
        return_str += u"Representative name for the entity: {}".format(entity.name) + "\n"
        return_str += u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name) + "\n"
        return_str += u"Salience score: {}".format(entity.salience) + "\n"
        for metadata_name, metadata_value in entity.metadata.items():
            return_str += u"{}: {}".format(metadata_name, metadata_value) + "\n"
        for mention in entity.mentions:
            return_str += u"Mention text: {}".format(mention.text.content) + "\n"
            return_str += u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name) + "\n"
    return_str += u"Language of the text: {}".format(response.language) + "\n"
    return return_str

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    return_str = ""
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        return_str += "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
    return_str += "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    return return_str

def sentiment_analysis(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})
    return print_result(annotations)

client = language_v1.LanguageServiceClient()

with open(sys.argv[1], 'r') as data_file:
    json_data = data_file.read()

data = json.loads(json_data)
N = 7
filename = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
with open(filename+".txt", 'w') as wrda:
    for d in data:
        wrda.writelines("-----------\n")
        wrda.writelines(entity_analysis(d['text']))
        wrda.writelines("\n")
        wrda.writelines(sentiment_analysis(d['text']))
        wrda.writelines("\n-----------\n")

print("Program executed. Check the text file: " + filename + ".txt")