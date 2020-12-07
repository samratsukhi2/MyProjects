import PyPDF2
import re
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
from spacy.lang.en import English
import nltk
nlp = en_core_web_sm.load()
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer 
lem = WordNetLemmatizer()
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english')) 

def strl(l):
    t=''
    for i in l:
        t+=str(i)+' '
    return t    

def wordcount(s):
    s=s.split(' ')
    return len(s)
    
def writefile(filename,text):
    f=open(filename,'w')
    text=text.lower()
    f.write(text)
    f.close()

def textFromPDF(pdf,text):
    wr=open(text,'w')
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range(15,pdfReader.numPages):
        page=pdfReader.getPage(i).extractText()
        s=re.sub('[^A-Za-z]+', ' ', page)
        wr.write('{}\n'.format(s))
    wr.close()
    pdfFileObj.close()

def getText(filename):
    f=open(filename,'r')
    line=''
    for i in f:
        line=line+' '+i
    return line
    f.close()

def texttoFreq(text):
    l=[]
    fr=[]
    for i in list(text.split(' ')):
        i=i.lower()
        if i not in l:
            l.append(i)
            fr.append(1)
        else:
            fr[l.index(i)]+=1    
    l=list(reversed(sorted(zip(fr,l))))
    ll=[]
    for i in l:
        ll.append(i[1])
    return strl(ll)

def coreWords(t):
    t=lem.lemmatize(t)
    t = nltk.word_tokenize(t)
    l=nltk.pos_tag(t)
    s=''
    for i in l:
        if len(i[0])!=1 and (i[1]=='NN' or i[1]=='VB' or i[1]=='NNS' or i[1]=='VBP' or i[1]=='JJ'):
            s+=i[0]+" " 
        else:
            print(i)    
    return s 

def findPure(a,b,lin=0):
    t=getText(a)
    l=[]
    t=t.split(' ')
    for i in t:
        if wordnet.synsets(i) and len(i)!=1:
            l.append(i)
        # else:
        #     print(i)
    t=''
    
    j=0
    if lin==0:
        lin=len(l)
    for i in l:
        if j==lin:
            break
        t+=i+' '
        j+=1
    writefile(b,t)    

def tokentester(t):
    t = nltk.word_tokenize(t)
    l=nltk.pos_tag(t)
    return l

def removetoken(t):
    lo=[]
    tr=[]
    ek=['NN','NNS','NNP','NNPS']
    for i in tokentester(t):
        
        if i[1] in ek and len(i[0])!=1:
            lo.append(i[0]) 
    return strl(lo)   

def finfreq(t1,t2,f):
    t1=t1.split(' ')
    t2=t2.split(' ')
    l=[]
    for i in t1:
        if i in t2:
            l.append(i)
    writefile(f,strl(l))        

def enlist(a):
    l=[]
    for i in a:
        i=i.split(' ')
        if i[0] not in l and i[0] not in stop_words:
            l.append(i[0])
        if i[0] not in l and i[1] not in stop_words:
            l.append(i[1]) 
    return l        

def mainwords(d):
    t=getText(d)
    l=[]

    l.append(re.findall(r'\w* is \w*',t))
    l.append(re.findall(r'\w* is not \w*',t))
    l.append(re.findall(r'of \w*',t))
    l.append(re.findall(r'\w* of',t))

    t=[]
    for i in l:
        t.extend(enlist(i))
    l=[]    
    for i in t:
        if i not in l:
            l.append(i)           
    t=strl(l)
    return t

