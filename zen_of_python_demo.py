#1 Beautiful is better than ugly:

def isPathExists(source, destination):
    if source == destination:
        return true
    else:                           # this can be removed
        for v in adj[source]:
            .....





#2 Explicit is better than implicit

#implicit
with open('kalman_results.csv', 'a', newline='') as file:
    .....

#explicit
kf_results_file = 'kalman_results.csv'
with open(kf_results_file, 'a', newline='') as file:
    .....





#3 Simple is better than complex

#complex code
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#simple code
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans





#4 Complex is better than complicated 

#complicated
i = 0
while i < 5:
   print(i)
   i += 1

#complex
for i in xrange(5):
   print(i)



    

#5 Flat is better than nested 

#nested
if condition1:
    if condition2:
        ....
    else:
        return
else:
    return

#flat
if not condition1:
    return
if not condition2:
    return
....






#6 Sparse is better than dense

The above example can be considered, I suppose

or

# dense
print('\n'.join("%i bytes = %i bits which has %i possible values." % (j, j*8, 256**j-1) for j in (1 << i for i in range(8))))

#sparse
bytes_and_bits = {j: j*8 for j in (1 << i for i in range(8))}

for bytes, bits in bytes_and_bits.items():
    print(f"{bytes} bytes = {bits} which has {256**bytes-1} possible values")






#7 Readability counts

#poor readability
x=10;y=20;z=x+y;print(z)

#readable
x = 10
y = 20
z = x + y
print(z)





#8 Special cases aren’t special enough to break the rules

#poor unnecessary special case
def area_of_rectangle(length, width):
    if length == 0:
        area = 0
    else:
        area = length * width
    return area

#well-written
def area_of_rectangle(length, width):
    return length * width





#9 Although practicality beats purity

#pure way
def subtract_32(fahrenheit):
    return fahrenheit - 32

def multiply_5_9(num):
    return num * 5/9

def fahrenheit_to_celsius(fahrenheit):
    temp = subtract_32(fahrenheit)
    return multiply_5_9(temp)

#practical way
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9






#10 Errors should never pass silently 

#poor
def divide(a, b):
    return a / b

res = divide(10, 0)

#well-written
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

res = divide(10, 0)





#11 Unless explicitly silenced

#poor
try:
    res = 10 / 0
except:
    pass

#well-written
try:
    res = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)





#12 In the face of ambiguity, refuse the temptation to guess

#poor (trying to mask the issue)
def add(a, b):
    if type(a) == str:
        a = int(a)
    if type(b) == str:
        b = int(b)
    return a + b

res = add("10", "20x")

#well-written 
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

res = add("10", "20x")



#13 There should be one - and preferably only one - obvious way to do it 

#obvious way to get sum of a list
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)
print(total)







#14 Although that way may not be obvious at first unless you're Dutch

#poor
def multiply(numbers):
    res = 1
    for number in numbers:
        res *= number
    return res

#well-written
from functools import reduce
def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)






#15 Now is better than never

#worser
i, j = 0, 0
while i < 100000: # doing some time consuming pre-processing that might hang
    j += 1
N = input()

#might be bad
N = input()
i, j = 0, 0
while i < 100000: # doing some time consuming pre-processing. Fixed the hang
    i += 1





#16 Although never is often better than *right* now


# Better to wait for the program execution rather than to terminate it early






#17 If the implementation is hard to explain, it’s a bad idea

#poor unnecessary implementation might be hard to explain
def calculate_sum_of_numbers(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum


#well-written
def calculate_sum_of_numbers(numbers):
    return sum(numbers)





#18 If the implementation is easy to explain, it may be a good idea

Similar to above, I suppose.





#19 Namespaces are one honking great idea - let’s do more of those!



a = 2
print('id(a) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

#output
id(a) = 9302208
id(a) = 9302240
id(3) = 9302240

#Unique name for each object


