f_i = open("D:\\rafid-console\input4.txt", "r")
var = int(f_i.readline())
f_o = open("D:\\rafid-console\output4.txt", "w")

dummy = []
#taking the eachline in a list
lst = f_i.readlines()
for i in range(len(lst)):
    lst[i] = lst[i].strip("\n")
#taking the first word of each line in a dummy list
for i in range(len(lst)):
    if lst[i].split(" ")[0] in dummy:
        continue
    else:
        dummy.append(lst[i].split(" ")[0])
#sort the list using insertion sort
for j in range(1, len(dummy)):
    key = dummy[j]
    i = j-1
    while i >= 0 and key < dummy[i]:
        dummy[i+1] = dummy[i]
        i -= 1
    dummy[i+1] = key

for i in dummy:
    for j in lst:
        if i == j.split(" ")[0]:
            f_o.write(j + "\n")

f_i.close()
f_o.close()
