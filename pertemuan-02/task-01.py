def oddDetector(var):
    return var % 2 == 0

def simpleCalc():
    num1 = int(input("Number 1 :"))
    num2 = int(input("Number 2 :"))

    select = str(input("Operation = 1.(/) 2.(*) 3.(-) 4.(+)\n>"))

    match(select):
        case '1':
            result = num1 / num2
        case '2':
            result = num1 * num2
        case '3':
            result = num1 - num2
        case '4':
            result = num1 + num2

    if (oddDetector(result) == True):
        print(f"\nResult : {result}\nThe number is Even\n")
    else:
        print(f"\nResult : {result}\nThe number is Odd\n")

while (True):
    do = str(input("Run program? (y/n)\n>"))
    match(do):
        case 'y':
            try:
                simpleCalc()
            except ZeroDivisionError:
                print("Can't divide 0 with 0\n")
        case 'n':
            print("Okay")
            break
        case default:
            print("Invalid input!")

