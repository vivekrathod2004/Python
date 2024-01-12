# if statement
num1 = int(input("Enter the first number: "))
if num1 > 0:
    print(f"{num1} is a positive number.")

# if-else statement
num2 = int(input("Enter the second number: "))
if num2 % 2 == 0:
    print(f"{num2} is an even number.")
else:
    print(f"{num2} is an odd number.")

# Nested if statements
num3 = int(input("Enter the third number: "))
if num3 > 0:
    print(f"{num3} is a positive number.")
    if num3 % 2 == 0:
        print(f"{num3} is also an even number.")
    else:
        print(f"{num3} is an odd number.")
elif num3 == 0:
    print("You entered zero.")
else:
    print(f"{num3} is a negative number.")

# if-elif statements
num4 = int(input("Enter the fourth number: "))
num5 = int(input("Enter the fifth number: "))
num6 = int(input("Enter the sixth number: "))
if num4 > num5 and num4 > num6:
    print(f"{num4} is the largest number.")
elif num4 > num5 and num4 > num6:
    print(f"{num4} is the largest number.")
else:
    print(f"{num6} is the largest number.")


# For loop
print("\n\nCounting from 1 to 10 using a for loop:")
for i in range(10):
    print(i)

print("\nEven-Odd\n")
num7=int(input("Enter the number 8 : "))

if num7%2==0:
    print(f"{num7} is even")
else:
    print(f"{num7} is odd")