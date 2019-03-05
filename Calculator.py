def add(x,y):
    print("{} + {} = ".format(x,y),x+y)
def subtract(x,y):
    print(x, "-" , y, "=" , x-y)
def multiply(x,y):
    print(x, "*" , y, "=" , x*y)
def divide(x,y):
    try:
        print(x, "/" , y, "=" , x/y)
    except:
        print("Error!")


def display(x,y):
    print("Operations : \n1: To add numbers\n2: To subtract numbers\n"
          "3: To multiply numbers\n4: To divide numbers")
    op = int(input("\n Enter value:"))
    if op == 1:
        add(x, y)
    elif op == 2:
        subtract(x, y)
    elif op == 3:
        multiply(x, y)
    elif op == 4:
        divide(x, y)
    else:
        print("Invalid option ")
        display(x,y);

    print("1: Reset\n2: For Previous Menu\n3: Exit")
    opp = int(input())
    if opp == 1:
        main()
    elif opp == 2:
        display(x,y)
    elif opp == 3:
        exit()

def main():
    print("Welcome to the Calculator")
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    display(x,y)



main()
