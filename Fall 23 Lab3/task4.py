def maxvalue(arr, n):
    m = float('-inf')
    maxsum = float('-inf')

    for i in range(n):
        maxsum = max(maxsum, m + pow(arr[i], 2))
        m = max(m, arr[i])

    return maxsum

f_i = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\input4.txt", "r")
f_o = open("G:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\output4.txt", "w")

num = int(f_i.readline())
nums = f_i.readline().split()
nums = [int(i) for i in nums]

max = maxvalue(nums, num)

f_o.write(str(max))

f_i.close()
f_o.close()
