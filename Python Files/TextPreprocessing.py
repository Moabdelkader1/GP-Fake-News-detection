import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import unicodedata as ud
from nltk.stem.isri import ISRIStemmer


st = ISRIStemmer()
stopwords_list=stopwords.words('arabic')


def preprocess_text(text):
    t = ''.join(c for c in text if not ud.category(c).startswith('P'))
    textwords = nltk.word_tokenize(t)
    filteredsentences = []
    # print(textwords)
    for w in textwords:
        if w not in stopwords_list:
            filteredsentences.append(w)
    stem = []
    # print(filteredsentences)
    for l in filteredsentences:
        stem.append(st.stem(l))
    listToStr = ' '.join([str(elem) for elem in stem])
    return listToStr


def applytfidf(textdoc):
    vectorizer = TfidfVectorizer(max_features=20000)
    vectorizer.fit(textdoc)
    idf = vectorizer.idf_
    # print(dict(zip(vectorizer.get_feature_names_out(), idf)))
    tfidf_matrix = vectorizer.transform(textdoc)
    n_components = 1000
    svd = TruncatedSVD(n_components=n_components)
    reduced_matrix = svd.fit_transform(tfidf_matrix)
    return tfidf_matrix,reduced_matrix

def applytfidf_1string(text):
    vectorizer = TfidfVectorizer(max_features=20000)
    #idf = vectorizer.idf_
    # print(dict(zip(vectorizer.get_feature_names_out(), idf)))
    tfidf_matrix = vectorizer.fit_transform(text)
    # n_components = 1000
    # svd = TruncatedSVD(n_components=n_components)
    # reduced_matrix = svd.fit_transform(tfidf_matrix)
    reduced_matrix=tfidf_matrix
    return tfidf_matrix, reduced_matrix