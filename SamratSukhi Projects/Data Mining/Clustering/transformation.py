f=open('dataset.csv','r')
t=0
lt=''
tt=0
ltt=''
l=[]
tl=[]
for i,ff in enumerate(f):
    if i==0:
        continue
    ff=ff.split(',')
    if ff[0]!=lt:
        lt=ff[0]
        t+=1
    if ff[3] not in tl:
        tl.append(ff[3]
        )  
    l.append(str(str(t)+' '+ff[1]+' '+ff[2]+' '+str(tl.index(ff[3])+1)))
ff=open('Data.txt','w')
for i in l:
    ff.write('{}\n'.format(i))