# Special diamond pattern with following conditions
        # Single For Loop
        # Single if else if ladder
        # Only 3 variables in whole program
num = int(input())
row_controller = 1 - num
i = 1

while row_controller < num:
    if i < abs(row_controller) + 1:
        print(" " , end = "")
        i += 1
    elif i < 2 * num - (1 + abs(row_controller)):
        print( "*" , end = "")
        i += 1
    else:
        print("*")
        i = 1
        row_controller += 1
