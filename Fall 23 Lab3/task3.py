<<<<<<< Updated upstream
def merge(arr, t, left, mid, right):
    i = left
    j = mid + 1
    k = left

    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            t[k] = arr[i]
            i += 1
        else:
            t[k] = arr[j]
            count += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        t[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        t[k] = arr[j]
        j += 1
        k += 1

    for x in range(left, right + 1):
        arr[x] = t[x]

    return count



def mrgsort(arr, t, left, right):
    count = 0

    if left < right:
        mid = (left + right) // 2
        count += mrgsort(arr, t, left, mid)
        count += mrgsort(arr, t, mid + 1, right)
        count += merge(arr, t, left, mid, right)

    return count



def cnt_inv(arr):
    n = len(arr)
    t = [0] * n
    return mrgsort(arr, t, 0, n - 1)

f_i = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\input3.txt", "r")
f_o = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\output3.txt", "w")

num = int(f_i.readline())
nums = f_i.readline().split()
nums = [int(i) for i in nums]

max = cnt_inv(nums)

f_o.write(str(max))
    
f_i.close()
f_o.close()

=======
count = 0
for i in range(n):
  for j in range(i+1,n):
    if H[i] > H[j]:
      count+=1
>>>>>>> Stashed changes
