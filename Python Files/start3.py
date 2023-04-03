import json
import os
import nltk
import unicodedata as ud
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.isri import ISRIStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import train_test_split
import pandas as pd
from tqdm import tqdm
from keras.models import Sequential
from keras.layers import Embedding,LSTM,Dense

import TextPreprocessing
import training_model















labeledData=pd.read_csv('labeled_data.csv')
unlabeledData=pd.read_csv('unlabeled_data.csv')

st = ISRIStemmer()

list_string=[]
print(len(labeledData))
samples=labeledData.sample(frac=0.04,random_state=50,ignore_index=True)

samples['label']=samples['label'].replace(['not credible','credible'],[0,1])
#print(samples['label'])
ysamples=samples['label']
print(len(samples))
num=0
#print(samples)
for i in tqdm(range(len(samples))):
    #print(labeledData.loc[i,'text'])
    title = samples.loc[i,'title']
    text=samples.loc[i,'text']
    published_date = samples.loc[i,'publishing_date']
    listToStr=TextPreprocessing.preprocess_text(text)
    #print(len(listToStr))
    num+=len(listToStr)
    #print(stem)
    #print(listToStr)
    samples.loc[i,'preprocessed_text']=listToStr

    #list_string.append(listToStr)
    #labeledData[i,'preprocessed_str']=listToStr
    #print(stem)
    #print(len(list_string))
    #exit()

avg=num/len(samples)
print("average="+str(avg))
textdoc=samples['preprocessed_text']
tfidf_matrix,reduced_matrix=TextPreprocessing.applytfidf(textdoc)
print(reduced_matrix.shape)
print(tfidf_matrix.get_shape())



#num_features=tfidf_matrix.get_shape()[1]
num_features=reduced_matrix.shape[1]




#model=training_model.create_model1(num_features)
model=training_model.create_model1(num_features)
tfidf_int=tfidf_matrix.toarray().astype('int32')
#reduced_matrix_int=reduced_matrix.toarray().astype('int32')
#print(len(tfidf_int))
#model.fit(tfidf_int,ysamples,epochs=5,verbose=1)
X_train,X_test,Y_train,Y_test=train_test_split(reduced_matrix,ysamples,test_size=0.2,random_state=20)


model.fit(X_train,Y_train,validation_data=(X_test,Y_test),epochs=1,verbose=1)
model.save('rnn.h5')
#model.fit(reduced_matrix,ysamples,epochs=5,verbose=1)


# model=Sequential()
# model.add(Embedding(input_dim=num_features,output_dim=50))
# model.add(LSTM(units=64))
# model.add(Dense(2,activation='softmax'))
#
# model.summary()
#
#
# model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])




# for i in tqdm(range(len(labeledData))):
#     #print(labeledData.loc[i,'text'])
#     title = labeledData.loc[i,'title']
#     text=labeledData.loc[i,'text']
#     published_date = labeledData.loc[i,'publishing_date']
#     t = ''.join(c for c in text if not ud.category(c).startswith('P'))
#     textwords = nltk.word_tokenize(t)
#     filteredsentences = [w for w in textwords]
#     filteredsentences=[]
#     #print(textwords)
#     for w in textwords:
#         if w not in stopwords_list:
#             filteredsentences.append(w)
#     stem=[]
#     #print(filteredsentences)
#     for l in filteredsentences:
#         stem.append(st.stem(l))
#     listToStr = ' '.join([str(elem) for elem in stem])
#     #print(stem)
#     #print(listToStr)
#     labeledData.loc[i,'preprocessed_text']=listToStr
#
#     #list_string.append(listToStr)
#     #labeledData[i,'preprocessed_str']=listToStr
#     #print(stem)
#     #print(len(list_string))
#     #exit()
#
#
# textdoc=labeledData['preprocessed_text']
# vectorizer = TfidfVectorizer(max_features=1000)
# vectorizer.fit(textdoc)
# idf = vectorizer.idf_
# print(dict(zip(vectorizer.get_feature_names_out(), idf)))


# print(list_string)
# print(len(list_string))


#
# for dirname,_,filnames in os.walk('AFND\AFND\Dataset'):
#     for filename in filnames:
#         path = os.path.join(dirname, filename)
#         # print(dirname)
#         source_path=dirname.split('\\')
#         print(source_path[-1])
#         #print(data.get(source_path[-1]))
#         article = open(path, encoding="utf8")
#         article_data = json.load(article)
#         overalldata.append(article_data)
#         tf_idf = []
#         list_string = []
#
#         # print(path)
#         for i in article_data["articles"]:
#
#             t = ''.join(c for c in text if not ud.category(c).startswith('P'))
#             published_date=i["published date"]
#             if (data.get(source_path[-1]) == "credible" or data.get(source_path[-1]) == "not credible"):
#                 source_num = source_path[-1]
#                 new_row={'title':title,'text':text,'publishing_date':published_date,'source_num':source_num,'label':data.get(source_path[-1])}
#                 datacsvlabeled=datacsvlabeled.append(new_row,ignore_index=True)
#             else:
#                 source_num = source_path[-1]
#                 new_row = {'title': title, 'text': text, 'publishing_date': published_date, 'source_num': source_num}
#                 datacsvunlabeled = datacsvunlabeled.append(new_row, ignore_index=True)
#             textwords=nltk.word_tokenize(t)
#             #print(textwords)
#             #print(textwords)
#             filteredsentences = [w for w in textwords]
#             filteredsentences=[]
#             for w in textwords:
#                 if w not in stopwords_list:
#                    filteredsentences.append(w)
#             stem=[]
#             for l in filteredsentences:
#
#                stem.append(st.stem(l))
#
#
#             # print(stem)
#             #print(filteredsentences)
#             listToStr = ' '.join([str(elem) for elem in stem])
#             list_string.append(listToStr)
#
#
#
#         vectorizer = TfidfVectorizer()
#         vectorizer.fit_transform(list_string)
#         idf = vectorizer.idf_
#         #print(dict(zip(vectorizer.get_feature_names_out(), idf)))
#         # print(tf_idf)
#
#
# datacsvlabeled.to_csv('labeled_data.csv',index=False)
# datacsvunlabeled.to_csv('unlabeled_data.csv',index=False)
# article.close()