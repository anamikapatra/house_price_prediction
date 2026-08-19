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


# Day 3
# Medium Level 
# Q:1
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()    
# for i in range(n-1,-1,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()    


# Q:2
# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")

#     print()


# Q:3
# n = 5
# for i in range(5,-1,-1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")

#     print()


# Q:4
# n = 4
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()


# Q:5
# n = 4
# num = 0
# for i in range(1, n + 1):
#     for j in range(i):
#         print(chr(65+num), end=" ")
#         num += 1
#     print()


# Q:6
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Q:7
 