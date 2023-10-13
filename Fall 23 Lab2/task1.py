f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab2\input1.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab2\output1.txt", "w")
rng, num = f_i.readline().strip().split(" ")
rng = int(rng)
num = int(num)
arr = f_i.readline().strip().split(" ")
arr = [int(i) for i in arr]
flag = "IMPOSSIBLE"

#solve with O(n^2) complexity
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == num:
            flag = str(i+1) + " " + str(j+1)
            break
        else:
            continue
    if flag != "IMPOSSIBLE":
        break

#solve with O(n) complexity
i = 0
j = rng-1
while i < j:
    if arr[i] + arr[j] == num:
        flag = str(i+1) + " " + str(j+1)
        break
    elif arr[i] + arr[j] > num:
        j -= 1
    else:
        i += 1

f_o.write(flag)

f_i.close()
f_o.close()
