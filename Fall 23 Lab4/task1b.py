f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\input1b.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\output1b.txt", "w")

n,m= map(int, f_i.readline().split())
n=n+1
# printing adjacency list of size n
adj_list= [[] for i in range(n)]

for i in range(m):
    u,v,w= map(int, f_i.readline().split())
    adj_list[u].append((v,w))

for i in range(n):
    f_o.write(str(i)+" : ")
    for j in range(len(adj_list[i])):
        f_o.write(str(adj_list[i][j])+" ")
    f_o.write("\n")

f_i.close()
f_o.close()


# Sample Input 1
# 4 3
# 1 3 8
# 3 2 5
# 1 4 2


# Sample Output 1
# 0 :
# 1 : (3,8) (4,2)
# 2 :
# 3 : (2,5)
# 4 :
