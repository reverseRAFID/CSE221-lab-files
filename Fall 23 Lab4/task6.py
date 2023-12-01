f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\input6.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab4\output6.txt", "w")

m,n=map(int,f_i.readline().split())
grid = []
for i in range(m):
    grid.append(f_i.readline().strip("\n"))
def dfs(row, col, visited):
    if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '#' or visited[row][col]:
        return 0
    visited[row][col] = True
    diamonds = 0
    if grid[row][col] == 'D':
        diamonds = 1
    diamonds += dfs(row+1, col, visited)
    diamonds += dfs(row-1, col, visited)
    diamonds += dfs(row, col+1, visited)
    diamonds += dfs(row, col-1, visited)
    return diamonds



def find_diamond():
    max_diamonds = 0
    visited = [[False] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'D':
                diamonds = dfs(i, j, visited)
                if diamonds > max_diamonds:
                    max_diamonds = diamonds
    return max_diamonds
f_o.writelines(f"{find_diamond()}")