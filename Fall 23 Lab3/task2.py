f_input = open("D:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\input2.txt", "r")
f_output = open("D:\\rafid-console\\CSE221-lab-files\\Fall 23 Lab3\\output2.txt", "w")

N = int(f_input.readline())
arr = f_input.readline().strip().split(" ")
for i in range(N):
  arr[i] = int(arr[i])
  
#complexity O(n)
maxValue = arr[0]
for i in range(1,N):
  if maxValue < arr[i]:
    maxValue = arr[i]

f_output.write(str(maxValue))

f_input.close()
f_output.close()
