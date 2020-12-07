import csv
f=open('Data.csv','r')
f1=open('IntData.txt','w')
fr=csv.reader(f)

a1=[]
t1=[]
u1=[]
r1=[]
m1=[]
v1=[]

####### Record Collected ##########
for i in fr:
    l=list(str(i).split(';'))
    p=l[0]
    p=p[2:]
    if p not in a1:
        a1.append(p)
    p=l[1]
    p=p[1:]
    if p not in t1:
        t1.append(p)
    if l[2] not in m1:
        m1.append(l[2])
    if l[3] not in u1:
        u1.append(l[3])
    if l[4] not in v1:
        v1.append(l[4])
    l[5]=str(l[5])[:-2]
    if l[5] not in r1:
        r1.append(l[5])

###### Writing data in Int Format#####
f.seek(0,0)

i=0
t=0
u=0
m=0
v=0
r=0

for i in fr:
    l=list(str(i).split(';'))
    p=l[0]
    p=p[2:]
    i=a1.index(p)+1

    p=l[1]
    p=p[1:]
    t=t1.index(p)+1

    m=m1.index(l[2])+1
    u=u1.index(l[3])+1
    v=v1.index(l[4])+1

    l[5]=str(l[5])[:-2]
    r=r1.index(l[5])+1

    f1.write("{} {} {} {} {} {}\n".format(i,t,m,u,v,r))
f.close() 
f1.close()
