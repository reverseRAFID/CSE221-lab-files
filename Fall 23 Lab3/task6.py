def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

def quicksort(arr, start, end, k):
    if start <= end:
      pivot_idx = partition(arr,start,end)

      if pivot_idx == k:
        return arr[k-1]
      if k < pivot_idx:
        return quicksort(arr, start, pivot_idx-1, k)
      else:
        return quicksort(arr, pivot_idx+1, end, k)
      
def partition(arr, i, j):
    pivot = arr[j]

    for k in range(i,j):
      if arr[k] <= pivot:
        swap(arr, k, i)
        i+=1

    swap(arr, j, i)
    return i

f_i=open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\input6.txt",'r')
f_o=open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\output6.txt",'w')
s = f_i.readline().split()
s=int(s[0])

lst=[int(i) for i in (f_i.readline()).split()]

s1 = f_i.readline().split()
s1 = int(s1[0])

for i in f_i:
    out = quicksort(lst,0,s-1,int(i))
    f_o.writelines(str(out)+ "\n")

f_i.close()
f_o.close()

# Sample Input 1
# 9 
# 10 11 10 6 7 9 8 15 2
# 4 
# 5
# 3
# 2
# 7


# Sample Output 1
# 9
# 7
# 6
# 10
