import csv

f=open('Data.csv','r')
f2=open('IntData.txt','w')
f3=open('detail.txt','w')
s=''
j=0
fr=csv.reader(f)
ip=[]
ts=[]
me=[]
req=[]
res=[]
byt=[]

for i in fr:
    s=str(i)
    s=list(s.split(' '))
    if len(s)!=6:
        continue
    if s[0] not in ip:
        ip.append(s[0])
    if s[1] not in ts:
        ts.append(s[1]) 
    if s[2] not in me:
        me.append(s[2])  
    if s[3] not in req:
        req.append(s[3]) 
    if s[4] not in res:
        res.append(s[4])    
    if s[5] not in byt:
        byt.append(s[5])

f.seek(0,0)
f3.write('{} {} {} {} {} {}'.format(len(ip),len(ts),len(me),len(req),len(res),len(byt)))
for i in fr:
    s=str(i)
    s=list(s.split(' '))
    if len(s)!=6:
        continue
    f2.write('{} {} {} {} {} {}\n'.format(ip.index(s[0])+1,ts.index(s[1])+1,me.index(s[2])+1,req.index(s[3])+1,res.index(s[4])+1,byt.index(s[5])+1))

f.close()
f2.close()
f3.close()