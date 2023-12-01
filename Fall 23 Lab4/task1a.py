f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\input1a.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\output1a.txt", "w")
n,m= map(int, f_i.readline().split())
n=n+1
#printing adjacency matrix of size n*n
adj_mat= [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    u,v,w= map(int, f_i.readline().split())
    adj_mat[u][v]= w

for i in range(n):
    for j in range(n):
        f_o.write(str(adj_mat[i][j])+" ")
    f_o.write("\n")

f_i.close()
f_o.close()
