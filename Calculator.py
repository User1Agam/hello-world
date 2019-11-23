
print("\033[1m" "\nWelcome. This is a simple calculator programmed by Agam Bhatti. This can compute basic arithmetic functions.\nTo begin, please select the number of the operation you would like to do below.\n")

# This program makes a simple calculator that can add, substract, multiply, and divide

# Define function (adds two numbers)

def add(x, y):
    return x + y

# define function subtracts two numbers

def subtract (x, y):
    return x - y

# define function multiplies two numbers

def multiply (x, y):
    return x * y

# define function (divides two numbers)
def divide (x, y):
    return x / y

print ("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user

choice = input("Enter choice (1,2,3,4): ")

num1 = float(input("Enter Your First Number: "))
num2 = float(input("Enter Your Second Number: "))

if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

if choice == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))










