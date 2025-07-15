# Write a program if number is positive or not
# num = int(input("Enter a number : "))
# if num > 0:
#     print('It is a positive number')
# elif num < 0:
#     print('It is a negative number')
# else:
#     print('Number is 0')


# Wap to find if number is even or odd
# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print('It is an even number')
# else:
#     print('It is an odd number')


# Wap to create an area calculator
# print("---------Area Calculator----------")
# print("""Press 1 to calculate area of square
# Press 2 to calculate area of rectangle
# Press 3 to calculate area of circle
# Press 4 to calculate area of triangle\n""")

# option = int(input("Enter whose area you want to calculate ? : "))
# print()
# if option == 1:
#     side = float(input("Enter the side of square : "))
#     area = side * side
#     print("\nArea of square : ",area)
# elif option == 2:
#     length = float(input("Enter the length of rectangle : "))
#     width = float(input("Enter the width of rectangle : "))
#     area = length * width
#     print("\nArea of rectangle : ",area)
# elif option == 3:
#     radius = float(input("Enter the radius of circle : "))
#     area = 3.1415926535 * radius * radius
#     print("\nArea of circle : ",area)
# elif option == 4:
#     base = float(input("Enter the base of triangle : "))
#     height = float(input("Enter the height of triangle : "))
#     area = 0.5 * base * height
#     print("\nArea of triangle : ",area)
# else:
#     print('Select the correct option!!')


# wap to calculate sum of all even numbers upto 50
# sum = 0
# for i in range(0,51,2):
#     sum = sum + i
# print('Sum of even numbers upto 50 : ',sum)


# wap to write first 20 numbers and their squared value
# for i in range(1,21):
#     print('Square of',i,':',i**2)


# wap to find sum of first 10 odd numbers
# sum = 0
# i = 0
# while i <= 20:
#     if i % 2 != 0:
#         sum += i
#     i += 1
# print('Sum oif first 10 odd numbers :',sum)


#  wap to check divisibility by 8 & 12 upto 100 numbers
# for i in range(0,101):
#     if (i % 8 == 0) and (i % 12 == 0):
#         print(i,'is divisible by 8 and 12')
#     else:
#         continue


# wap to create a bill of supermarket
# while True:
#     name = input('Enter the name of the customer : ')
#     total = 0

#     while True:
#         qty = int(input('Enter the quantity of the item : '))
#         amt = float(input('Enter the amount of the item : '))
#         total += qty * amt
#         repeat = input('Do you want to add more items (y/n) : ')
        
#         if repeat == 'n':
#             break
    
#     print('\n')
#     print('-'*40)
#     print('******Welcome to Sukhjas mart*******')
#     print('-'*40)
#     print('Name :',name)
#     print('Amount to be paid :',total)
#     print('-'*40)
#     print('***********Happy Shopping**********\n')

#     repeat1 = input('Do you want to go to next customer (y/n) : ')

#     if repeat1 == 'n' or repeat == 'n':
#         break


# a = 'Why fit in, When you are Born to Stand Out!'

# wap to find the length of the following string 
# print('The length of the string a is :',len(a))


# wap to calculate how many times letter o occurs in the string
# print('Number of times o occurs : ',a.count('o'))


# wap to convert the whole string into lower or upper case
# print('Lower cased string :',a.lower())
# print('Upper cased string :',a.upper())


# wap to convert the whole string into a title
# print('Title :',a.title())


# wap to find the index of 'fit in' from the string
# print('Index :',a.find('fit in'))


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#  wap to print the pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# wap to print this pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end = " ")
#     print()


# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4
# 5
# wap to print this pattern
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i,end = " ")
#     print()

#     *
#    **
#   ***
#  ****
# ***** 
# wap to print this pattern
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*",end = " ")
#     print()


# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# wap to print this pattern
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end = " ")
#     print()


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# wap to print this pattern
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end = "")
#     print()


# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# wap to print this pattern
# for i in range(1,8):
#     for j in range(1,i+1):  
#         print(i*j,end = " ")
#     print()


# wap to find the fibonacci series upto 10 numbers
# a = 0
# b = 1
# n = int(input('Enter the number upto which you want the fibonacci series : '))
# if n == 1:
#     print(1)
# else:
#     print('The fibonacci series upto',n,'numbers : ')
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


# wap to check if the number is prime or not 
# num = int(input('Enter the number : '))
# if num <= 1:
#     print('It is not a prime number')
# elif num == 2:
#     print('It is a prime number')
# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print('It is not a prime number')
#             break
#     else:
#         print('It is a prime number')


# wap to check for the palindrome
# num = int(input('Enter the number : '))
# temp = num
# rev = 0
# while temp > 0:
#     n = temp % 10
#     rev = rev * 10 + n
#     temp = temp // 10
# if rev == num:
#     print('It is a palindrome')
# else:
#     print('It is not a palindrome')


# A = "OOTD.YOLO.ASAP.BRB.GTG.OTW" 

# wap to separate the following sri ng into coma(,) separated coma
# print(A.split('.'))


# wap to sort strings alphabeticaly
# print(sorted(A)) 


# wap to remove a given character from a string  
# a = "hello"
# b = a.replace("e","")
# print(b)


# z = "F.R.I.E.N.D.S"
# wap to remove '.' from the string
# print(z.replace(".",''))


# A = ["Ross","Rachel","Monica","Joe"]
# wap to swap first and fourth element
# A[0],A[3] = A[3],A[0]
# print(A)


# convert the following dict into json format
# import json
# student_data = {"name":"Sukhman","age":20,"marks":99.5}
# print(type(student_data))
# data = json.dumps(student_data)
# print(data)
# print(type(data))


# access the value of age from the given json data
# import json
# student_data = """{"name": "David","age":13,"marks":99}"""
# data = json.loads(student_data)
# print(data["age"])


# pretty print following json data
# import json
# student_data = {"name":"Sukhman","age":20,"marks":99.5}
# data = json.dumps(student_data,indent=4,separators=(",","="))
# print(data)


# sort the following json keys and write them into a file
# import json
# student_data = {"name":"Sukhman","age":20,"marks":99.5}
# f = open("demo.json",'w')
# data = json.dumps(student_data,indent=4,sort_keys=True)
# f.write(data)
# print('The data has been added to the file')


# Access the nested key "marks" from the following nested data
# import json
# student_data = """{"student":{
#     "grade":{
#         "name":"David",
#         "marks":95
#     }
# }}"""
# data = json.loads(student_data)
# print(data["student"]["grade"]["marks"])


# wap to sort a dict by value
# a = {'a':12,'b':15,'c':20,'d':30,'e':25}
# a = sorted(a.values())
# print(a)


# wap to print a dict where keys are numbers b/w 1-15 and values are their square
# a = {}
# for i in range(1,16):
#     a[i] = i**2

# print(a)


# wap to multiply all the items in a dict
# a = {'a':12,'b':15,'c':20,'d':30,'e':25}
# product = 1
# for i in a:
#     product *= a[i]
# print(product)


# wap to sort a dict by keys
# a = {'a':12,'b':15,'c':20,'d':30,'e':25}
# a = sorted(a.keys())
# print(a)


# lambda
# a = lambda b: b*5
# print(a(4))


# x = lambda a,b,c: (a+b)*c
# print(x(2,3,5))


# waf to find maximum of 3 numbers
# def maxNumber(a,b,c):
#     if (a > b) and (a > c):
#         print(a,'is greatest number')
#     elif (b > a) and (b > c):
#         print(b,'is greatest number')
#     else:
#         print(c,'is greatest number')

# maxNumber(3,6,2)


# waf to create and print a list where the values are squares of numbers b/w 1 and 30
# def create_list():
#     l = []
#     for i in range(1,31):
#         l.append(i**2)
#     return l

# print(create_list())


# waf that takes a number as a parameter and check if it is prime or not
# def checkPrime(a):
#     if a == 1:
#         print("It is not a prime number")
#     if a == 2:
#         print("It is a prime number")
#     if a > 2:
#         for i in range(2,a):
#             if a % i == 0:
#                 print("It is not a prime number")
#                 break
#         else:
#             print("It is a prime number")   

# checkPrime(17)


# waf to sum all the numbers in the list
# def sum_list(l):
#     total = 0
#     for i in l:
#         total += i
#     return total

# print(sum_list([20,30,40,50]))


# using datetime module
# import datetime
# x = datetime.datetime(2004,10,13)
# print(x)
# print(x.strftime("%D"))


# using random module
# import random
# x = random.randint(1,6)
# print(x)

# a = ['heads','tails']
# x = random.choice(a)
# print(x)


# using math module
# import math
# x = max(13,67,46)
# print(x)
# y = min(13,67,46)
# print(y)
# a = pow(2,3)
# print(a)
# b = math.sqrt(8)
# print(b)
# c = abs(-12.345)
# print(c)
# d = math.ceil(2.4)
# print(d)
# e = math.floor(3.6)
# print(e)