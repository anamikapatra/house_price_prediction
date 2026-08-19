# Day 2 Assingnment(Topics: if-elif-else,nestde if-else)\
# Low level Assignment(Beginner)

# #Q:1
# num=int(input("enter a number:-"))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")    


# Q:2
# num=int(input("enter a number: "))
# if num==0:
#     print("Zero Number")
# elif num>0:
#     print("Positive Number")
# else:
#     print("Negative Number")    


# Q:3
# number=int(input("Enter a number:-"))
# if number%5==0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5") 


# Q:4
# number=int(input("enter a number:"))
# if number%2==0 and number%5==0:
#     print("number is divible by 10")
# else:
#     print("Not divisible by 10")


# Q:5
# character=input("enter a string:")
# if character.isalpha():
#     print("Alphabet")
# else:
#     print("Not alphabet")


# Q:6
# user_input=input("enter a string:")
# vowel=0
# conso=0
# for i in user_input:
#     if (i>='a' and i<='z') or (i>='A' and i<='Z'):
#         if i in "aeiouAEIOU":
#             vowel=vowel+1
#         else:
#             conso=conso+1 
# print(vowel,conso)     



# # Q:7
# person=int(input("Enter a number:- "))
# if person>=18:
#     print("Eligible for voting")
# else:
#     print("not eligible for voting")



# Q:8
# num=int(input("enter a number: "))
# if num>=1 and num<=100:
#     print("The number is within the range 1 to 100.")
# else:
#     print("The number is outside the range 1 to 100.")   



# Q:9
# num=int(input("enter a number: "))
# if(num %5==0) and (num%11==0):
#     print("A number is divisible by 5 nad 11")
# else:
#     print("A number is not divisible by 5 and 11") 



# Q:10
# num=int(input("enter a number: "))
# if num>50:
#     print("A number is greater than 50")
# else:
#     print("A number is less than 50") 



# Q:11
# marks=56
# if marks>35:
#     print("Pass 😊")
# else:
#     print("Fail 😔")    



# Q:12
# charac=input("enter a string:- ")
# if charac.isupper():
#     print("Character is uppercase")
# elif charac.islower():
#     print("character is lower case")
# else:
#     print("not an alphabet")    



# Q:13
# num=int(input("enter a number: "))
# if num>10:
#     print("greater than 10")
# elif num==10:
#     print("equal")
# else:
#     print("less than 10") 



# Q:14
# num=6
# if num%2==0 and num%3==0:
#     print("A number is divisible by 2 and 3")
# else:
#     print("A number is not divisible by 2 and 3")   
 


# Q:15
# num=int(input("enter a number:- "))
# if num==0:
#     print("Zero")
# else:
#     print("Not equal zero")    





# 2. Medium Level Assignment (intermediate)
# Q:1
# num=int(input("enter a number:-"))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd") 



# Q:2
# year=int(input("enter a year: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("Leap year")
# else:
#     print("it is not a leap year")    



# Q:3
# marks=35
# if marks>=90:
#     print("Grade: O")
# elif marks>=80 and marks<90:
#     print("Grade: E") 
# elif marks>=70 and marks<80:
#     print("Grade: AA")   
# elif marks>=60 and marks<70:
#     print("Grade: A")
# elif marks>=50 and marks<60:
#     print("Grade: B")
# elif marks>=35 and marks<50:
#     print("Grade: C")                
# else:
#     print("Fail")    



# Q:4
# a=7
# b=16
# c=95
# if a>b and a>c:
#     print("A is a largest number")
# elif b>a and b>c:
#     print("B is a largest number")
# else:
#     print("C is a largest number")        



# Q:5
# day = int(input("Enter a number (1-7): "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid input")



# Q:6
# person=int(input("enter a age="))
# if person<13:
#     print("Cild")
# elif person>=13 and person<18:
#     print("teenager")    
# else:
#     print("Adult")



# Q:8
# i=input("Enter a string:- ")
# if (i>='a' and i<='z') or (i>='A' and i<='Z'):
#     if i.isupper():
#         print("uppercase")
#     elif i.islower():
#         print("lowercase")
#     else:
#         print("neither")
# else:
#     print("not alphabet")                



# Q:9
# num=float(input("Enter a number: "))
# if 10<= num <=50:
#     print(f"{num} is between 10 and 50")
# else:
#     print(f"{num} is not between 10 and 50")    



# Q:10
# a=int(input("Enter a 1st number: "))
# if a<180:
#     b=int(input("Enter a 2nd number: "))
#     if a+b <180:
#         c=int(input("Enter a 3rd number: "))
#         if a+b+c ==180:
#             print("valid triangle")
#         else:
#             print("invalid input c")
#     else:
#         print("invalid input b")
# else:
#     print("invalid input a")    



# Q:11
# a=int(input("enter a number: "))
# if a%3==0 and a%7==0:
#     print("both is divisible by 3 and 7")
# else:
#     print("not divisible by 3 and 7")




# Q:12
# num1=int(input("enter a num1: "))
# num2=int(input("enter a num2: "))
# if num1>num2:
#     print("greater num1")
# elif num2>num1:
#     print("greater num2 ")
# else:
#     print("both are qual")




# Q:13
# num=int(input("enter a number: "))
# if num>=0 and num%2==0:
#     print('number is positive and even')
# elif num>=0 and num%2!=0:
#     print(" positive but not even ")
# else:
#     print('neither positive nor even')    



# Q:14
# num=int(input("enter a number:- "))
# if num<0:
#     print("negative")
# elif num%5==0:
#     print("divisible by 5")    
# else:
#     print("neither negative nor divisible")    



# Q:15
# tempa=float(input("enter a temperature: "))
# if tempa<10:
#     print("Cold")
# elif tempa>=10 and tempa<25:
#     print("moderate") 
# else:
#     print('Hot')       




# High Level Assignments (Advanced)
# Q:1
# num=int(input("enter a number: "))
# if num%2==0:
#     print("divisible by 2")
#     if num%3==0:
#         print("divisible by 3")
#     else:
#         print("not divisible by 3")
# else:
#     print("not divisible by 2")    





# Q:2
# num=int(input("enter a number:- "))
# if num>0:
#     print("Number is positive")
#     if num%2==0:
#         print("Also  number is Even number")
#     else:
#         print("But number is odd number")
# else:
#     print("not positive")     



# Q:3
# marks = float(input("Enter marks: "))
# if marks >= 0 and marks <= 100:  
#     if marks >= 90:
#         print("Grade: A")
#     else:
#         if marks >= 75:
#             print("Grade: B")
#         else:
#             if marks >= 50:
#                 print("Grade: C")
#             else:
#                 print("Grade: Fail")               
# else:
#     print("Invalid marks")



# Q:4
# a=9
# b=89
# c=-9
# if a>b:
#     if a>c:
#         print("Largest number is ",a)
#     else:
#         print("largest number is ",c)
# else:
#     if b>c:
#         print("largest number is ",b)
#     else:
#         print("largest number is ", c)                





# Q:5
# year=int(input("Enter a Year:- "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")




# Q:6
# a=int(input("enter a number: "))
# b=int(input("enter a number : "))
# op=input("Enter Operator(+,-,/,*): ")
# if op=='+':
#     print("Result= ",a+b)
# else:
#     if op=='-':
#         print("Result= ",a-b)
#     else:
#         if op=='*':
#             print("Result= ",a*b)
#         else:
#             if op=='/':
#                 if b!=0:
#                     print("Result= ",a/b)
#                 else:
#                     print("Not divisible by zero")
#             else:
#                 print("Invalid operator")            




# Q:7
# username=input("Enter name: ")
# password=int(input("Enter number: "))

# correct_username="Anamika Patra"
# correct_password=1234
# if username==correct_username:
#     if password==correct_password:
#         print("Login Successfuly")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid UsernameA")            



# Q:8
# user_input=input("enter a Alphabet: ")
# if user_input.isalpha():
#     if user_input in 'AEIOUaeiou':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Not alphabet")            





# Q:9
# num=int(input("Enetr number range (1-100): "))
# if num>=1 and num<=100:
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("number is out of range")            



# Q:10
# num=int(input("enter a number: "))
# if num>=0:
#     if num%2==0:
#         print("even number")
#     else:
#         print("odd number")
# else:
#     print("negative number")            



# Q:11
# amount = float(input("Enter total amount: "))

# if amount > 5000:
#     discount = amount * 0.20
#     final_amount = amount - discount
#     print("20% discount applied")
    
# else:
#     if amount > 2000:
#         discount = amount * 0.10
#         final_amount = amount - discount
#         print("10% discount applied")
        
#     else:
#         discount = 0
#         final_amount = amount
#         print("No discount")

# print("Discount:", discount)
# print("Final amount to pay:", final_amount)
     




# Q:12
# marks=int(input("enter a student marks: "))
# if marks>=35:
#     print("Pass")
#     if marks>=75:
#         print("Distinction")
#     else:
#         print("Normal pass")
# else:
#     print("Fail")            



# Q:13
# num=int(input("enter a number: "))
# if num%5==0:
#     if num%11==0:
#         print("divisible by both")
#     else:
#         print("Not divisible by 11")
# else:
#     print("not divisible by 5")



# Q:15
a=float(input('Enter side 1:- '))
b=float(input(('enter side 2:- ')))
c=float(input('enter side 3:- '))
if a+b>c and b+c>a and c+a>b:
    print('valid triangle')
    if a==b==c:
        print('equilateral')
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

else:
    print("Not a Valid Triangle")