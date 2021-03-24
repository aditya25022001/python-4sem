import math

# Question 1 input name and print with hello
name = input("What is your name ? ")
age = int(input("What is your age ? "))
age+=5
print("Hello " + name + " your age after five years : " + age)

# Area of circle
diameter = float(input("diameter of circle : "))
area = math.pi*(diameter**2)/4
print(area)

# Print numbers from 0 to 10
for x in range(11):
    print(x)

# ask name from user
name = input("Enter name : ")
if(name):
    print("Welcome "+name)
else:
    print("Welcome unknown")

# Print all perfect squares in range of 1 - 1000
a = 1
while(a**2 < 1000):
    print(a**2)
    a += 1

# 1-1000
for i in range(1, 1001, 2):
    print(i)

# Print type of each value in list
list = [1, 2, 'geeks', 4, 6, 'geeks']
for each in list:
    print(type(each))

# create list of table 10
list = [10*x for x in range(1, 13)]
print(list)
list2 = ['hello', 'geeks']
list.append(list2)
print(list)
print(list[-1])
print(list[-1][-1])
print(len(list))
print(list[len(list)-1])
print(list[len(list)-1][len(list2)-1])
# #
