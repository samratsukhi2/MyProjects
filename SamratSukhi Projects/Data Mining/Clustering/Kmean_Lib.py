from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

f=open('Data.txt','r')
l=[]
k=3
for i in f:
    i=i.split(' ')
    l.append([i[2],i[3]])

df=pd.DataFrame(l)

km=KMeans(n_clusters=k,random_state=0).fit(df)
ykm=km.fit_predict(df)
print(km.cluster_centers_)

# plt.scatter(df[0], df[1], c=ykm, s=50, cmap='viridis')
# centers = km.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='r', s=200, alpha=0.5);
# plt.show()