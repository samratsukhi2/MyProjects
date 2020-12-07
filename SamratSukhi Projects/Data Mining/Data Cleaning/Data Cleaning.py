import csv

f=open('data.csv','r')
f2=open('cleaned_data.csv','w')
fr=csv.reader(f)

for i in fr:
    
    if (str(i)[2]).isdigit():
        f2.write('{}\n'.format(str(*i)))
    else:
        print(str(i))
f.close()
f2.write('')
f2.close()
