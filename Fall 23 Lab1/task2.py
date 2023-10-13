f_i = open("D:\\rafid-console\input2.txt", "r")
var = int(f_i.readline())
f_o = open("D:\\rafid-console\output2.txt", "w")

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                flag = 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if flag == 0:
            break
    return arr


arr = f_i.readline().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])

out = bubbleSort(arr)
for i in range(len(out)):
    f_o.write(str(out[i]) + " ")


f_i.close()
f_o.close()

#Generally bubble sort runs on O(n^2) time complexity. 
# if the data is already sorted then it will run on O(n) time complexity, 
# which is known as best case scenerio. Hence to achieve O(n) time complexity, 
# we can add a flag to check if the data is already sorted or not. 
# If the data is already sorted then we can break the loop and return the data.
