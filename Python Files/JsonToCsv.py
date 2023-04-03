import pandas as pd
import json
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


datacsvlabeled=pd.DataFrame(columns=['title','text','publishing_date','source_num','label'])
datacsvunlabeled=pd.DataFrame(columns=['title','text','publishing_date','source_num'])
path="AFND\AFND\sources.json"
#print(path)
file=open(path)
data=json.load(file)
file.close()
for dirname,_,filnames in os.walk('AFND\AFND\Dataset'):
    for filename in filnames:
        path = os.path.join(dirname, filename)
        source_path=dirname.split('\\')
        print(source_path[-1])
        article = open(path, encoding="utf8")
        article_data = json.load(article)
        for i in article_data["articles"]:
            title=i["title"]
            text=i["text"]
            published_date=i["published date"]
            if (data.get(source_path[-1]) == "credible" or data.get(source_path[-1]) == "not credible"):
                source_num = source_path[-1]
                new_row={'title':title,'text':text,'publishing_date':published_date,'source_num':source_num,'label':data.get(source_path[-1])}
                datacsvlabeled=datacsvlabeled.append(new_row,ignore_index=True)
            else:
                source_num = source_path[-1]
                new_row = {'title': title, 'text': text, 'publishing_date': published_date, 'source_num': source_num}
                datacsvunlabeled = datacsvunlabeled.append(new_row, ignore_index=True)
            print(datacsvlabeled)
datacsvlabeled.to_csv('labeled_data.csv',index=False)
datacsvunlabeled.to_csv('unlabeled_data.csv',index=False)
article.close()



