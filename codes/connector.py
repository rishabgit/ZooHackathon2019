import pandas as pd
import numpy as np
from spellchecker import SpellChecker
from googletrans import Translator
from nltk.corpus import wordnet

sc=SpellChecker()
translator = Translator()
tags=[]
month_adds=[0]*12
maxi=0
mini=100000000

def split_string(string):
    return string.split()
def checklanguage(string):
    language = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
    }
    lang=translator.translate(string).src
    if(lang=='en'):
        return [language[str(lang)],1]
    else:
        return [language[str(lang)],0]

def translate(string,dest='en',src='auto'):
    return(translator.translate(string,dest=dest,src=src).text)

def check_typos(string):
    if(checklanguage(string)[1]==0):
        string=translate(string)
    else:
        pass
    l_co=[]
    string=string.split()
    for i in string:
        cw=sc.correction(i)
        l_co.append(cw)
    return l_co

def find_nouns(string):
    l=[]
    for i in string:
        syns = wordnet.synsets(i)
        if((syns[0].lexname().split('.')[0]) if syns else (w, None)=='noun'):
            l.append(i)
            
    return l
    
    
def main_run(string):
    string=check_typos(string)
    for i in range(len(string)):
        string[i]=string[i].capitalize()
    return string
    


#code
import pandas as pd
import numpy as np

df=pd.read_csv('data_final.csv')
col1=np.array(df['Species'])
col2=np.array(df['Common name'])
col3=np.array(df['Scientific name'])
col4=np.array(df['Price'])
col5=np.array(df['months'])
l=[0,0,0]
index=[]#the length will give the total advertisements
m_prices=0#will be a list containing the month prices

def process(string):
    for i in string:
        if(i in col1):
            l[0]=1
        if(i in col2):
            l[1]=1
        if(i in col3):
            l[2]=1
    plist=[00.00]*12

    if(l[0]==1):
        for i in range(len(col1)):
            if(string[0] in col1[i]):
                index.append(i)
                p=col4[i]
                m=int(col5[i])
                try:
                    plist[m]=plist[m]+float(p[1:])
                    if(float(p[1:])>maxi):
                        maxi=float(p[1:])
                    
                    if(float(p[1:])<mini):
                        mini=float(p[1:])
                        
                except:
                    plist[m]=plist[m]+0
                month_adds[m]=month_adds[m]+1
    elif(l[1]==1):
        for i in range(len(col2)):
            if(string[0] in col2[i]):
                index.append(i)
                p=col4[i]
                m=col5[i]
                try:
                    plist[m]=plist[m]+float(p[1:])
                    if(float(p[1:])>maxi):
                        maxi=float(p[1:])
                    
                    if(float(p[1:])<mini and float(p[1:])!=0):
                        mini=float(p[1:])
                except:
                    plist[m]=plist[m]+0
                month_adds[m]=month_adds[m]+1
    else:
        for i in range(len(col2)):
            if(string[0] in col2[i]):
                index.append(i)
                p=col4[i]
                m=col5[i]
                try:
                    plist[m]=plist[m]+float(p[1:])
                    if(float(p[1:])>=maxi):
                        maxi=float(p[1:])
                    
                    if(float(p[1:])<=mini):
                        mini=float(p[1:])
                except:
                    plist[m]=plist[m]+0
                month_adds[m]=month_adds[m]+1
    return plist

tags=main_run("Pinkbelly Snapping Turtle")
m_prices=process(tags)
print("the tags are")
print(tags)
print("the month prices")
print(m_prices)
print("the total number of advertisements")
print(len(index))
print("the number of adds per month are")
print(month_adds)
print("the max is")
print(maxi)
print("the min is")
print(mini)

def data(string):
    tags=main_run(string)
    m_prices=process(tags)
    print("the tags are")
    print(tags)
    print("the month prices")
    print(m_prices)
    print("the total number of advertisements")
    print(len(index))
    print("the number of adds per month are")
    print(month_adds)
    return tags,m_prices,len(index),month_adds,maxi,mini
