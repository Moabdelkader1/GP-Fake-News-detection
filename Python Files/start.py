import json
import os
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
stopwords_list=stopwords.words('arabic')
print(stopwords_list)
#nltk.download('punkt')

# labelspath="AFND\AFND\sources.json"
# # print(labelspath)
# labelsfile=open(labelspath)
# labelsdata=json.load(labelsfile)
# labelsfile.close()

# for i in labelsdata:
#     print(i+":"+labelsdata[i])
overalldata=[]
for dirname,_,filnames in os.walk('AFND\AFND\Dataset'):
    for filename in filnames:
        path = os.path.join(dirname, filename)
        print(path)
        article = open(path,encoding="utf8")
        article_data = json.load(article)

        overalldata.append(article_data)
        # for i in article_data["articles"]:
        #     title=i["title"]
        #     text=i["text"]
        #     published_date=i["published date"]
        #     textwords=nltk.word_tokenize(text)
        #     #print("text:" + text)
        #     print(textwords)

            # print("text:"+)
            # print("published date:"+)
        os.exit()
        article.close()



