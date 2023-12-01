f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\input5.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\output5.txt", "w")

#The given map will be an undirected and unweighted graph.
#find the shortest path 
#Print the minimum amount of time to reach city D from city 1.
#Next, print the shortest path you will follow.

n,m,k=map(int,f_i.readline().split())
graph={}
for i in range(n):
    graph[i+1]=[]
for i in range(m):
    u,v=map(int,f_i.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[0]*(n+1)
visited[1]=1
queue=[]
queue.append(1)
parent=[0]*(n+1)
while queue:
    u=queue.pop(0)
    for v in graph[u]:
        if visited[v]==0:
            visited[v]=1
            parent[v]=u
            queue.append(v)
path=[]
v=k
while v!=0:
    path.append(v)
    v=parent[v]
path.reverse()
f_o.write("Time: "+str(len(path)-1)+"\n")
f_o.write("Shortest Path: ")

for i in path:
    f_o.write(str(i)+" ")
f_o.close()
f_i.close()



# Sample input:
# 4 3 2
# 1 3
# 3 2
# 1 4

# Sample output:
# Time: 2
# Shortest Path: 1 3 2
