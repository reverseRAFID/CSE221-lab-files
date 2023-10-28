def quick(arr):
    if len(arr) <= 1:
        return arr

    num = arr[len(arr)//2]

    left = []
    mid = []
    right = []

    for i in arr:
        if i < num:
            left.append(i)
        if i == num:
            mid.append(i)
        if i > num:
            right.append(i)

    sorted = quick(left) + mid + quick(right)

    return sorted

f_i = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\input5.txt", "r")
f_o = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\output5.txt", "w")

N = int(f_i.readline())

nums =  f_i.readline().split()
nums = [int(i) for i in nums]

new = quick(nums)

for i in new:
    f_o.write(str(i) + " ")

f_i.close()
f_o.close()
