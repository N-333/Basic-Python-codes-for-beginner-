# 1. Program to check if a number is positive using an if statement. 

num = int(input("Enter a number : "))
if num>0:
    print(f"{num} is positive")


# 2. Program to check if the number is positive or negative using if-else.

num = int(input("Enter a number : "))
if num>0:
    print(f"{num} is positive")
else :
    print(f"{num} is nega2tive")
    
# 3. Program to check if the number is positive, negative or zero  using if-elif-else.

num = int(input("Enter a number : "))
if num==0:
    print(f"{num} is zero")
elif num>0:
    print(f"{num} is  positive")
else :
    print(f"{num}is negative")
    
# 4. Program to check if a person is eligible to vote using if-else

Mark =int(input("Enter your age :"))
if Mark>18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

# 5. Program to check if the number is even or odd using if-else

num = int(input("Enter a number : ")) 
if num%2==0:
    print(f"{num} is a even number")
else :
    print(f"{num} is an odd number")
    
# 6. Program to check if the year is leap year using if-else

year= int(input("Enter a year :"))
if year%4 == 0 and year%400 == 0:
    print(f"{year} is a leap year ")
else :
    print(f"{year} is not a leap year")
    
#  7. Program to classify a person's age group using if-else.

Mark = int(input("Enter the age : "))
if Mark<=13:
    print("You are a kid")
elif 13<Mark<=19:
    print("You are a teenager")
elif 19<Mark<=65:
    print("You are a adult")
else: 
    print("You are a senior citizen")
    
# 8. Program to check the largest of three numbers using nested if statements.

num1,num2,num3 = input("Enter three numbers : ").split()
if num1>num2 and num1>num3:
   print(f"{num1} is the largest number.")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number.")
else :
    print(f"{num3} is the largest number.")

# 9. Program to check if a number is divisible by 5 using if-else

num = int(input("Enter a number : ")) 
if num%5==0:
    print(f"{num} is divisible by 5")
else :
    print(f"{num} is not divisible by 5")
    
# 10. Program to check the grade of a student based on marks using if-elif-else.

Mark = int(input("Enter your mark : "))
if Mark>=80:
    print("Your grade : A")
elif 60<=Mark<80:
    print("Your grade : B")
elif 40<=Mark<60:
    print("Your grade : C")
elif 20<=Mark<40:
    print("Your grade : D")
else: 
    print("Your grade : E")
