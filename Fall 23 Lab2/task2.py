f_i= open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab2\\input2.txt", "r")
f_o= open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab2\\output2.txt", "w")

n= int(f_i.readline())
arr= f_i.readline().strip("\n").split()
for i in range(n):
    arr[i]= int(arr[i])

m= int(f_i.readline())
arr2= f_i.readline().strip("\n").split()
for i in range(m):
    arr2[i]= int(arr2[i])

#merge 2 sorted arrays using O(nlogn) time complexity,
#divide the array into 2 halves and recursively call the function
#and then merge the 2 arrays using merge function

def merge(arr, arr2):
    if len(arr) == 0:
        return arr2
    if len(arr2) == 0:
        return arr
    if arr[0] <= arr2[0]:
        return [arr[0]] + merge(arr[1:], arr2)
    else:
        return [arr2[0]] + merge(arr, arr2[1:])
arr3= merge(arr, arr2)
for i in range(len(arr3)):
    f_o.write(str(arr3[i])+" ")

#merge 2 sorted arrays using O(n) time complexity, 
#the theory is using 2 pointers in while loop and comparing the values of the 2 arrays 
#and appending the smaller one to the new array.


arr3= []
i= 0
j= 0
while i < len(arr) and j < len(arr2):
    if arr[i] <= arr2[j]:
        arr3.append(arr[i])
        i+= 1
    else:
        arr3.append(arr2[j])
        j+= 1
while i < len(arr):
    arr3.append(arr[i])
    i+= 1
while j < len(arr2):
    arr3.append(arr2[j])
    j+= 1
for i in range(len(arr3)):
    f_o.write(str(arr3[i])+" ")



f_i.close()
f_o.close()