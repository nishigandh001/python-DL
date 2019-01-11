from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.util import  ngrams
from collections import  Counter
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
from  nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer

url="https://en.wikipedia.org/wiki/Python_(programming_language)"
html=urllib.request.urlopen(url)
soup=BeautifulSoup(html,"html.parser")
data=soup.findAll(text=True)
for element in soup(['script','style','document','head','title']):
    element.extract()
text=soup.get_text()
print(text)
#print(text)
with open('output.txt','w+',encoding="UTF-8") as fp:
   fp.write(text)
#print(soup)

with open('output.txt','r',encoding="UTF-8") as token_file:
    print("Tokenizer")
    for i in token_file.readlines():
       # print(i)
        tokens=nltk.word_tokenize(i)
        # tokens=nltk.word_tokenize(token_file)
        print(tokens)

        # Parts Of Speech
        print(nltk.pos_tag(tokens))

        # Stemming the sentences
        singles=[]
        pStem= PorterStemmer()
        for p in i.split():
            singles.append(pStem.stem(p))
        print( ' '.join(singles))

        #Lemmetization
        lemmatizer=     WordNetLemmatizer()
        lemmatizer.lemmatize(i)
        print(lemmatizer)

        print("-----trigram---------")
        print(Counter(ngrams(nltk.word_tokenize(i), 3)))
        print("-----Name Entity Recognition---------")
        print(ne_chunk(pos_tag(wordpunct_tokenize(i))))

    stemmer = LancasterStemmer()
    stemmer1 = PorterStemmer()
    stemmer2 = SnowballStemmer('english')
    print("-----Lemmetization---------")
    lemmetizer = WordNetLemmatizer()
    for data in tokens:
        print("Lemmetizer for word: ", data, ": ", lemmetizer.lemmatize(data))
        print("Lancaster Stemming for word: ", data, ": ", stemmer.stem(data))
        print("Porter Stemming for word: ", data, ": ", stemmer1.stem(data))
        print("Snowball Stemming for word: ", data, ": ", stemmer2.stem(data))