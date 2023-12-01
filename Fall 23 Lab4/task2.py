f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\input2.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\output2.txt", "w")
n,m= map(int, f_i.readline().split())

graph= [[] for i in range(n+1)]
visited= [False for i in range(n+1)]
stack= []

for i in range(m):

    u,v= map(int, f_i.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(s):
    visited[s]= True
    queue= [s]
    while queue:
        s= queue.pop(0)
        stack.append(s)
        for i in graph[s]:
            if not visited[i]:
                queue.append(i)
                visited[i]= True

for i in range(1,n+1):

    if not visited[i]:
        bfs(i)

for i in stack:
    f_o.write(str(i)+" ")

f_i.close()
f_o.close()
