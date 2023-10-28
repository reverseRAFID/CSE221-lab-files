def merge(a, b):
# write your code here
# Here a and b are two sorted list
# merge function will return a sorted list after merging a and b

    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i < len(a):
        c.append(a[i])
        i+=1
    while j < len(b):
        c.append(b[j])
        j+=1
    return c


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])  # write the parameter 
        a2 = mergeSort(arr[mid:])  # write the parameter
        return merge(a1, a2)       # complete the merge function above 
    

f_input = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\input1.txt", "r")
f_output = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\output1.txt", "w")
var = f_input.readline().strip()
arr = f_input.readline().strip().split(" ")
for i in range(len(arr)):
    arr[i] = int(arr[i])

arr = mergeSort(arr)
for i in range(len(arr)):
    f_output.write(str(arr[i]) + " ")
f_input.close()
f_output.close()