#python3
import json
from textblob import TextBlob

with open('data.json') as json_data:
    d = json.load(json_data)
    for i in range(len(d)):
	    pos = 0
	    neg = 0
	    neu = 0
	    total = 0
	    print(d[i]["name"],"\n")
	    for j in range(len(d[i]["reviews"])):
		    text = d[i]["reviews"][j]["review_text"]
		    blob = TextBlob(text)
            #for sentence in blob.sentences:
                #print(sentence.sentiment.polarity)
		    if blob.sentiment.polarity > 0:
			    pos = pos + 1
			    print('positive')
		    elif blob.sentiment.polarity == 0:
			    neu = neu + 1
			    print('neutral')
		    else:
			    neg = neg + 1
			    print('negative')
	    total = pos + neu + neg
	    print('% of Positive', (pos/total)*100)
	    print('% of Negative', (neg/total)*100)
	    print('% of Neutral', (neu/total)*100)
