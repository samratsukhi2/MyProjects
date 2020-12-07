import csv

f=open('Log.csv','r')
f2=open('cleaned_data.csv','w')
fr=csv.reader(f)

ip=''
ts=''
ofs=''
me=""
req=""
sta=""
byt=""
ref=""
bro=""
l=""

for i in fr:
    l=str(i)
    l=list(l.split(' '))
    try:

        #IP Address
        l[0]=str(l[0])[2:]
        ip=l[0]
        
        #host name
        #user name
        #Time Stamp
        l[3]=str(l[3])[1:]
        ts=l[3]

        #offset
        #Method
        me=str(l[5])[1:]

        #request URL
        req=str(l[6])
        
        #protocol
        #status code
        sta=str(l[8])

        #bytes 
        byt=str(l[9])

        #reference 
        #Browser
        #Operating System
        
    except:
        continue
    f2.write('{} {} {} {} {} {}\n'.format(ip,ts,me,req,sta,byt))
       
f.close()
f2.close()
