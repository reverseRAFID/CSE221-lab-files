f_i = open("D:\\rafid-console\input3.txt", "r")
var = int(f_i.readline())
f_o = open("D:\\rafid-console\output3.txt", "w")

dic = {}
#creating a key value pair for each element in the array with the next line
key_arr = f_i.readline().strip("\n").split(" ")
val_arr = f_i.readline().strip("\n").split(" ")
# print(key_arr)
# print(val_arr)
for i in range(0, int(var)):
    key_arr[i] = int(key_arr[i])
    val_arr[i] = int(val_arr[i])
    dic[key_arr[i]] = val_arr[i]

#sorting the values in the dictionary in descending order using insertion sort
for i in range(1, len(dic)):
    key = key_arr[i]
    val = val_arr[i]
    j = i-1
    while j >= 0 and val > val_arr[j]:
        val_arr[j+1] = val_arr[j]
        key_arr[j+1] = key_arr[j]
        j -= 1
    val_arr[j+1] = val
    key_arr[j+1] = key
#sort the value containing same value in ascending order using insertion sort
for i in range(1, len(dic)):
    key = key_arr[i]
    val = val_arr[i]
    j = i-1
    while j >= 0 and val == val_arr[j] and key < key_arr[j]:
        val_arr[j+1] = val_arr[j]
        key_arr[j+1] = key_arr[j]
        j -= 1
    val_arr[j+1] = val
    key_arr[j+1] = key

#printing the sorted values
for i in range(0, len(dic)):
    f_o.write("ID: " +str(key_arr[i]) + " Mark: " + str(val_arr[i]) + "\n")

f_i.close()
f_o.close()