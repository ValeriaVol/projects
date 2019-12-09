import re
from string import punctuation
import nltk
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer
import pickle
from bs4 import BeautifulSoup
import requests
import os
page = requests.get('https://www.kinopoisk.ru/film/568289/ord/rating/perpage/200/#list')
parsed = BeautifulSoup (page.content, 'html.parser')
reviews = parsed.find_all("span", itemprop="reviewBody")
reviewstexts=[i.get_text() for i in reviews]
newpath = r'C:/Users/Валерия/reviews'
if not os.path.exists(newpath):
            os.makedirs(newpath)
with open(newpath + '\\'+ 'bohemian'+'.txt','a',encoding="utf-8") as of:
    for i in reviewstexts:
        of.writelines(i)

morph = MorphAnalyzer()
punct = punctuation + '«»—…“”*№–'
stops = stopwords.words('russian')
from nltk.tokenize import word_tokenize
stops.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на', 'хоть', 'после','который','свой','самый','каждый','чей'])

def normalize(text):
    words = [word.strip(punct) for word in word_tokenize(text.lower())]
    words = [morph.parse(word)[0].normal_form for word in words]
    words = [word for word in words if word not in stops]
    words = [word for word in words if word.endswith('й')]
    words = list(filter(None, words))
    return words

with open(r'C:\Users\EdUKUser\PycharmProjects\Module_A\Project' + '\\' + 'ekstaz.txt', 'r',encoding="utf-8") as openfile:
    content = openfile.read()
    contents_normalized = normalize(content)
    tokenized = contents_normalized
    freqdict = {i: tokenized.count(i) for i in set(tokenized)}
    #sorted_freq = sorted(freqdict.items(), key=lambda item: item[1],reverse=True)  # что сортируемfreqdict.items() по какому значению key=lambda х: х[1] (мы показы ваем, что мы сортируем по часточности, по тт
    #print(sorted_freq)
    #sorted_freq_list=[i for i in sorted_freq]
    #print(sorted_freq_list)

with open(r'C:\Users\EdUKUser\PycharmProjects\Module_A\Project' + '\\' + 'Эмоц прил.txt', 'r', encoding="utf-8") as file:
    dict_ = file.read()
    dict_clear = re.sub(r'\',?', '', dict_)
    dict1 = dict_clear.lower()[1:]
    emotional_list=dict1.split()
    dict_emotion = dict()

    for adj in freqdict:
        if adj in emotional_list:
            dict_emotion[adj] =freqdict[adj]
sorted_dict_emotion = sorted(dict_emotion.items(), key=lambda item: item[1],reverse=True)
print(sorted_dict_emotion)





