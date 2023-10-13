f_i= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab2\input1.txt", "r")
f_o= open("D:\\rafid-console\CSE221-lab-files\Fall 23 Lab2\output1.txt", "w")
rng, num = f_i.readline().strip().split(" ")
rng = int(rng)
num = int(num)
arr = f_i.readline().strip().split(" ")
arr = [int(i) for i in arr]
flag = "IMPOSSIBLE"
for j in range (rng):
    for k in range (rng):
        if arr[j] != arr[k] and arr[j] + arr[k] == num:
            flag = f"{j+1} {k+1}"
            break
f_o.write(flag)

f_i.close()
f_o.close()