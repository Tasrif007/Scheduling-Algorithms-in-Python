#!/usr/bin/env python
# coding: utf-8

# # Scheduling Algorithms
# **[This is Scheduling Algorithm implemented in python]**

# First Come First Serve

# In[ ]:


n = int (input("Enter no.of processess:"))
p = []
w = []
tw = 0
for i in range(n):
    p.append(int (input("Enter process:")))
    w.append(int (input("Enter weight:")))
    
d1 = dict(zip(p,w))
d2 = 0
weight = 0
print("Waiting time:")
for i, j in d1.items():
    print (i,"=",weight)
    d2 = d2 + weight
    weight = weight + j
   
print("Average waiting time: ",d2/n)

for i in d1.values():
     tw = tw + i
print("Average turn around time: ",(d2+tw)/n)


# Priority Scheduling

# In[ ]:


print("*****No two processes must have same priority*****",end = "\n")
n = int (input("Enter no.of processess:"))
p = []
w = []
tw = 0
for i in range(n):
    print("Process:",i,end="\n")
    p.append(int (input("Enter priority:")))
    w.append(int (input("Enter weight:")))
    
small = 9999
d1 = dict(zip(w,p))
d2 = dict()
for i in range(n):
    small = 9999
    for j in d1.keys():
        if(d1[j] < small):
            small = d1[j]
            t = j
    d1[t] = 9999
    d2[t] = small

d1 = d2
d2 = dict()
for i , j in d1.items():
    d2[j] = i

d1 = d2 
d2 = 0
print(d1)
weight = 0
print("Waiting time:")
for i, j in d1.items():
    print ("Process with ",i," priority has ",weight," waiting time")
    d2 = d2 + weight
    weight = weight + j
   
print("Average waiting time: ",d2/n)
for i in d1.values():
     tw = tw + i

print("Average turn around time: ",(d2+tw)/n)



# Round Robin Scheduling

# In[ ]:


n = int (input("Enter no.of processess:"))
q = int (input("Enter time quantum:"))
p = []
w = []
tw = 0
d2 = d3 = dict()  
for i in range(n):
    y = int (input("Enter process:"))
    p.append(y)
    j = int (input("Enter weight:"))
    w.append(j)
    tw = tw + j
    d2[y] = 0
d1 = dict(zip(p,w))
d3 = dict(zip(p,w))
t = s = 0
#print(d1,d2,d3)
print("Waiting time:")
while(tw != 0):
   for i in d1.keys():
      if(d1[i] >= q):
         tw = tw - q
         d1[i] = d1[i] - q
         t = t + q
         if(d1[i] == 0):
             d2[i] = t
      elif(d1[i] < q and d1[i] > 0):
         tw = tw - d1[i]
         t = t + d1[i] 
         d1[i] = 0
         d2[i] = t
t = 0
for i in d2.keys():
    d2[i] = d2[i] - d3[i]
    t = t + d2[i]
print(d2)


print("Average waiting time: ",t/n)

for i in d3.values():
     tw = tw + i
print("Average turn around time: ",(t+tw)/n)     


# Shortest Job First

# In[ ]:


n = int (input("Enter no.of processess:"))
p = []
w = []
tw = 0
for i in range(n):
    p.append(int (input("Enter process:")))
    w.append(int (input("Enter weight:")))
    
small = 9999
d1 = dict(zip(p,w))
d2 = dict()
for i in range(n):
    small = 9999
    for j in d1.keys():
        if(d1[j] < small):
            small = d1[j]
            t = j
    d1[t] = 9999
    d2[t] = small
    
    
d1 = d2
d2 = 0
print(d1)
weight = 0
print("Waiting time:")
for i, j in d1.items():
    print (i,"=",weight)
    d2 = d2 + weight
    weight = weight + j
   
print("Average waiting time: ",d2/n)
for i in d1.values():
     tw = tw + i

print("Average turn around time: ",(d2+tw)/n)

