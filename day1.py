# 1. Low Level Assignment(Beginner)
# Q:1
# name="Anamika Patra"
# print(name)

# Q:2
# age=21
# height=5.2
# print(type(age))
# print(type(height))

# Q:3
# a=5
# b=7
# c=a+b
# print("Add to number:",c)


# Q:4
# a=int(input("enter a 1st number:"))
# b=int(input("enter a 2nd number"))
# print("Addition:-",a+b)
# print("Subtraction:-",a-b)
# print("Multiplication:-",a*b)
# print("Division:-",a/b)

# Q:5
# a=9
# c=float(a)
# print("Before a type casting number:-",a)
# print("After a type Casting number:-",c)


# Q:6
# name=input("enter a string:-")
# print("Length:-",len(name))

# Q:7
# user_input = input("Enter a string: ")
# if user_input:
#     first_char = user_input[0]
#     print("The First character of the string is:", first_char)
# else:
#     print("The string is empty.")


# Q:8
# a="Anamika"
# b=" Patra"
# print("Concatenate two string:-",a+b)

# Q:9[pari ni]

# Q:10
# user=input("enter a string:-")
# if user:
#     last_char=user[-1:]
#     print(last_char)



# Medium Level Assignment(Intermediate)
# Q:1
# a=8
# b=9
# a=a+b
# b=a-b
# a=a-b
# print("Before without swapping the two numbers:-",a,b)
# print("after Swap number a:-",a)
# print("after Swap number b:-",b)

# Q:2
# num=int(input("enter a number:-"))
# if num%2!=0:
#     print("Odd number")
# else:
#     print("Even number")    

# Q:3
# value =78.9
# int_value=int(value)
# print(value)
# print(int_value)

# Q:4
# user_input=input("Enter a string:-")
# count=0
# for i in user_input:
#     count+=1
# print("Count a string:-",count)    

# Q:5
# user_input=input("Enter a string:-")
# reverse_string=user_input[::-1]
# print("Reverse string:-",reverse_string)


# Q:6
# user_input="HelloWorld!!!"
# five_char=user_input[:5]
# print("Extract the 5 characters:-",five_char)


# Q:7
# a="Hello"
# b="World"
# if a==b:
#     print("Equal")
# else:
#     print("not equal")    


# Q:8
# a='Hello world'
# print(a.replace("world","Anamika"))


# Q:9
# user_input=input("Enter a string:-")
# print(user_input[2:9])


# Q:10
# user=input("enter a string:-")
# vowel=0
# for i in user:
#     if (user>='a' and user<='z') or (user>='A' and user<='Z'):
#         if i in("aeiouAEIOU"):
#             vowel=vowel+1
  
# print("Vowel:-",vowel)


# High Level Assignment(Advanced)
# Q:1
# user=input("Enter name:-")
# str=user.split()
# f=''
# for i in str:
#     f=f+i[0]
# print(f)    

# Q:2
# e_mail="anamika40917@gmail.com"
# vowel=0
# conso=0
# digit=0
# special=0
# for i in e_mail:
#     if (i>='a' and i<='z') or (i>='A' and i<='Z'):
#         if i in "aeiouAEIOU":
#             vowel=vowel+1
#         else:
#             conso=conso+1
#     elif i.isdigit():
#         digit=digit+1
#     else:
#         special=special+1

# print("Vowel:-",vowel)
# print("Consonanats:-",conso)
# print("Digits:-",digit)
# print("Special Char:-",special)
        
# Q:3
# user="Dipak"
# str=''
# length=len(user)
# for i in range(length -1,-1,-1):
#     str=str+user[i]  
# print(str)    


# Q:4
# user_input=input("Enter Sentence:-")
# longest_sen=[]
# split_sen=user_input.split()
# for i in split_sen:




# Q:5
# num_str1="14"
# num_str2="5"
# number1=int(num_str1)
# number2=int(num_str2)
# print(number1,number2)
# print("Addition:-",number1+number2)
# print("Substraction:-",number1-number2)
# print("Multiply:-",number1*number2)
# print("Division:-",number1/number2)

# Q:6
# user_input = input("Enter a string:- ")
# no_spaces = user_input.replace(" ", "")
# print("Remove all space for string:", no_spaces)

# Q:7
# user_input=input("Enter a string:-")
# freq={}
# for i in user_input:
#     if (i>='a' and i<='z') or (i>='A' and i<='Z'):
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
# print(freq)            




# Q:8
# user=input("Enter name:-")
# str=user.split()
# f=''
# for i in str:
#     f=f+i[0].upper()
# print(f)

# Q:9
# user_input=input("Enter a sentence:-")
# words=user_input.split()
# for i in words:
#     print(i)



# Q:10
# user="Hello World"
# print(user[::2])