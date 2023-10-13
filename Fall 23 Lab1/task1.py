f = open("D:\\rafid-console\input1a.txt", "r")

var = int(f.readline())
f1 = open("D:\\rafid-console\output1a.txt", "w")
for i in range(var):
    test = int(f.readline())
    #create a new file and store the output
    result = "even" if int(test) % 2 == 0 else "odd"
    out = f"{test} is an {result} number.\n"
    f1.write(out)

f1.close()
f.close()