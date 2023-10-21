def interval(starttime, finishtime):

    index = list(range(len(starttime)))   # index for n items
    index.sort(key=lambda i: finishtime[i]) # sort according to finish times
 
    maximum_task = set()
    prev_ftime = 0
    for i in index:
        if starttime[i] >= prev_ftime:
            maximum_task.add((starttime[i],finishtime[i]))
            prev_ftime = finishtime[i]
 
    return maximum_task

def schedule_remover(set):
    cstart = 0
    cend = 0
    for i in set:
        for j in range(len(start)):
            if start[j] == i[0] and cstart < len(set):
                del start[j]
                cstart +=1
                break
            
        for x in range(len(end)):
            if end[x] == i[0] and cend < len(set):
                del end[x]
                cend += 1
                break
           
        


f_i = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab2\\input4.txt", "r")
f_o = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab2\\output4.txt", "w")

a, b = f_i.readline().split()
a, b = int(a), int(b)

start = []
end = []
taskcount = 0

for i in range(a):
    n1, n2 = f_i.readline().split()
    n1, n2 = int(n1), int(n2)
    start.append(n1)
    end.append(n2)

for i in range(b):
    tasks = interval(start,end)
    tasks = list(tasks)
    tasks.sort(key=lambda i: i[1])
    taskcount += len(tasks)
    schedule_remover(tasks)


f_o.writelines(f'{taskcount}')