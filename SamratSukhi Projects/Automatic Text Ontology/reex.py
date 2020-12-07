#REgular Expression File
# is
# is not
# is a 
# is an
# every can Be.
# every must be
# either or 
# if a is then 
import samrat as sam
import re

def apply(t,tt,o):
    l=re.findall(r'\w* will be \w* \w*',t) # apply
    k=['NN','NNS','NNP','NNPS']
    tt=tt.split(' ')
    j=[]
    text=[]
    for i in l:
        j=i.split(' ') 
        try:
            a=sam.tokentester(j[0])
            a=a[0]
            b=sam.tokentester(j[3])
            b=b[0]
            c=sam.tokentester(j[4])
            c=c[0]

            if a[1] in k and b[1] in k and c[1] in k and b[0] in tt and c[0] in tt and a[0] in tt:
                text.append((b[0],c[0],a[0]))
        except:
            continue 
    nt=''
    for i in text:
        nt+='<class> '+i[0]+' '+i[1]+'\n\t<subclass> '+i[2]+' </subclass>'+'\n</class>\n'
    sam.writefile(o,nt)

 
def siblings(t,tt,o):
    l=re.findall(r'\w* and \w*',t) # siblings
    k=['NN','NNS','NNP','NNPS']
    tt=tt.split(' ')
    j=[]
    text=[]
    for i in l:
        j=i.split(' ') 
        try:
            a=sam.tokentester(j[0])
            a=a[0]
            b=sam.tokentester(j[2])
            b=b[0]
            if a[1] in k and b[1] in k:
                text.append((a[0],b[0]))
        except:
            continue 
    nt=[]
    for i in text:
        y=str('<siblings> '+i[0]+','+i[1]+'</siblings>\n')
        if y not in nt:
            nt.append(y)
        nt.append(y)
    text=sam.strl(nt)    
    sam.writefile(o,text)  
    