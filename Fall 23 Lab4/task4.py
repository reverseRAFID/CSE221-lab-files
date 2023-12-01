f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\input4.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\output4.txt", "w")
n,m= map(int, f_i.readline().split())

graph={}
for i in range(1,n+1):
    graph[i]=[]
for i in range(m):
    node_1,node_2=map(int, f_i.readline().split())
    graph[node_1].append(node_2)
color={}
for i in graph.keys():
    color[i]="White"
def dfs(graph,vertex,color):
    color[vertex]="Gray"
    for neighbor in graph[vertex]:
        if color[neighbor]=="White":
            cycle_found=dfs(graph,neighbor,color)
            if cycle_found==True:
                return True
        elif color[neighbor]=="Gray":
            return True
    color[vertex]="Black"
    return False
def check_cycle(graph,color):
    cycle_found=False
    for vertex in graph.keys():
        if color[vertex]=="White":
            cycle_found=dfs(graph,vertex,color)
            if cycle_found==True:
                break
    return cycle_found

flag=check_cycle(graph,color)
if flag:
    f_o.writelines("YES")
else:
    f_o.writelines("NO")
f_i.close()
f_o.close()




# Sample input
# 4 3
# 1 3
# 3 2
# 1 4

# Sample Output 
# No