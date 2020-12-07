import matplotlib.pyplot as plt 

f=open("Intdata.txt",'r')
x=[]
y=[]
z=[]
for i in f:
    l=list(map(int,i.split()))
    x.append(l[3])
    y.append(l[1])
    z.append(l[0])
plt.plot(x, y,'ro') 
plt.xlabel('Files') 
plt.ylabel('Time Stamp') 
plt.title('File Access Graph') 
plt.show() 
