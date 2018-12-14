Num = int(input("Enter the number: "))
flag = Num%2
if flag == 0:
    print(Num, "is an even number")
elif flag == 1:
    print(Num, "is an odd number")
else:
    print("Error, Invalid input")
