import random
import math

def eucldist(a,b):
    dist = 0.0
    for i in range(0,len(a)):
        dist += (a[i] - b[i])**2
    return math.sqrt(dist)

def kmeans(k,datapoints):

    d = len(datapoints[0]) 
    MI = 1000
    i = 0
    cluster = [0] * len(datapoints)
    prev_cluster = [-1] * len(datapoints)
    cluster_centers = []

    for i in range(0,k):
        new_cluster = []
        for i in range(0,d):
           new_cluster += [random.randint(0,10)]
        cluster_centers += [random.choice(datapoints)]
        
    while (cluster != prev_cluster) or (i > MI) :

        prev_cluster = list(cluster)
        i += 1
        
        for p in range(0,len(datapoints)):
            min_dist = float("inf")
            for c in range(0,len(cluster_centers)):
                dist = eucldist(datapoints[p],cluster_centers[c])
                if (dist < min_dist):
                    min_dist = dist  
                    cluster[p] = c   
        
        
        #Update Cluster's Position
        for k in range(0,len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0,len(datapoints)):
                if (cluster[p] == k): #If this point belongs to the cluster
                    for j in range(0,d):
                        new_center[j] += datapoints[p][j]
                    members += 1
            
            for j in range(0,d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members) 
                else: 
                    new_center = random.choice(datapoints)                 
            cluster_centers[k] = new_center
    
        
    for i in cluster_centers:
        print(i)
    
    
f=open('Data.txt','r')
l=[]
k=3
for i in f:
    i=list(map(int,i.split(' ')))
    i=i[2:]
    l.append(i)
kmeans(k,l)