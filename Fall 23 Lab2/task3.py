f_i= open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab2\\input3.txt", "r")
f_o= open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab2\\output3.txt", "w")

def interval(starttime, finishtime):

    index = list(range(len(starttime)))   # index for n items
    index.sort(key=lambda i: finishtime[i]) # sort according to finish times
 
    maximal_set = set()
    prev_finish_time = 0
    for i in index:
        if starttime[i] >= prev_finish_time:
            maximal_set.add((starttime[i],finishtime[i]))
            prev_finish_time = finishtime[i]
 
    return maximal_set


a = f_i.readline()
a = int(a)

start = []
end = []

for i in range(a):
    n1, n2 = f_i.readline().split()
    n1, n2 = int(n1), int(n2)
    start.append(n1)
    end.append(n2)

total_tasks = interval(start,end)
total_tasks = list(total_tasks)
total_tasks.sort(key=lambda i: i[1])
print(total_tasks)
f_o.writelines(f'{len(total_tasks)}\n')
for i in total_tasks:
    for j in i:
        f_o.writelines(f'{j} ')
    f_o.writelines(f'\n')


f_i.close()
f_o.close()