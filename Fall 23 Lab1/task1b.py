f_i = open("D:\\rafid-console\input1b.txt", "r")
var = int(f_i.readline())
f_o = open("D:\\rafid-console\output1b.txt", "w")


operators = ["+", "-", "*", "/"]
for i in range(var):
    test = f_i.readline().split(" ")    
    test[3] = test[3].strip("\n")
    if test[2] in operators:
        if test[2] == "+":
            f_o.write(f"The result of {test[1]} {test[2]} {test[3]} is {str(int(test[1]) + int(test[3]))}\n")
        elif test[2] == "-":
            f_o.write(f"The result of {test[1]} {test[2]} {test[3]} is {str(int(test[1]) - int(test[3]))}\n")
        elif test[2] == "*":
            f_o.write(f"The result of {test[1]} {test[2]} {test[3]} is {str(int(test[1]) * int(test[3]))}\n")
        elif test[2] == "/":
            f_o.write(f"The result of {test[1]} {test[2]} {test[3]} is {str(int(test[1]) / int(test[3]))}\n")
    else:
        f_o.write(f"{test[2]} is not a valid operator\n")


f_i.close()
f_o.close()