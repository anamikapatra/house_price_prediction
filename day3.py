#1. Low Level Assignment (Beginner)
# Q:1
# for i in range(1,51):
#     print(i) 



# Q:2
# num=1
# while(num<=100):
#     print(num) 
#     num+=1



# Q:3
# num=100
# while(num>=1):
#     print(num) 
#     num-=1  



#Q:4
# for i in range(1,11):
#     print("Welcome")



# Q:5
# for i in range(2,51,2):
#     print(i)



# Q:6
# for i in range(1,51,2):
#     print(i)



# Q:7
# n=int(input("enter a number: "))
# print("Even" if n%2==0 else "odd")



# Q:8
# n=1
# while(n<=20):
#     if n==10:
#         break
#     print(n)
#     n+=1    



# Q:9
# for i in range(1,20,1):
#     if i==5:
#         continue
#     print(i)




# Q:10
# for i in range(1,6):
#     if i==3:
#         pass
#     else:
#         print(i)

   


# Q:11
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# Q:13
# num=int(input("enter a number: "))
# sum_digit=0
# temp=abs(num)
# while temp> 0:
#     rem = temp%10
#     sum_digit += rem
#     temp //= 10
# print(sum_digit)    






# Q:14
# n = int(input("Enter N: "))

# for i in range(1, n + 1):
#     if i % 5 == 0:
#         print(i, end=" ")




# Q:15
# text=input("enter a string: ")
# for index,char in enumerate(text):
#     print("Index",index,"Character",char)





# Pattern
# Q:1
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end='')
#     print()    




# Q:2
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end='')
#     print()    




# Q:3
# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()    


# Q:4
# n=4
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end='')
#     print()  


# Q:5
# rows=3
# col=5
# for i in range(1,rows+1):
#     for j in range(1,col+1):
#         print("*",end=" ")
#     print()


# 2.Medium Level Assignment(Intermediate)
# Q:1
# n=int(input("Enter a number: "))
# a=0
# b=1
# for i in range(n):
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c



# Q:2
# num=10
# while(num>0):
#     if num%2==0:
#         print(num)
#     num-=1


# Q:3
# num=10
# while(num>0):
#     if num%2!=0:
#         print(num)
#     num-=1


# Q:4
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)    


# Q:5
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)    


# Q:6
# num=int(input("enter a number: "))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not prime")                
             

#Q:7 
# num=int(input("enter a number: "))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not prime")       



# Q:8
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)    


# Q:9
# a=2
# b=5
# print("a is largest" if a>b else "b is largest")

# Q:10
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#     if i%7==0:
#         break
#     print(i)


# Q:11
# for i in range(1,20):
#     if i==3:
#         continue
#     print(i)


# Q:12
# num=20
# if num>0:
#     pass
# else:
#     print("num is not positive")
# print("Execute sucessfuly")   



# Q:13
# num=int(input("enter a number"))
# for i in range(1,11):
#     print(num, "*",i, "=",num*i)


# Q:15
# user=input("enter string: ")
# for index,chr in enumerate(user):
#     print("Index", index,"Character" ,chr)

# Q:14
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# for ch1, ch2 in zip(str1, str2):
#     print(ch1, "-", ch2)