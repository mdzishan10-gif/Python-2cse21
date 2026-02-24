# Program to print the sum of values from 1 to 5
print(1 + 2 + 3 + 4 + 5)

# Program to find sum of odd numbers from 1 to 100
N = 1
S = 0
while N <= 100:
    S = S + N
    N = N + 2
print(S)

#question02-2
if n % 2 == 0:
  So the completed code becomes:
  # Program to check whether a number is even or odd
print("Enter an integer:")
n = int(input())

if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")


# Program to print the required pattern 
print("*" * 20)
print("#" * 20)

# Q.04-01 Program to store and print name and address

name = "Md Zishan Alam"
address = "Greater Noida, India"

print(name)
print(address)

Given code:
x = 1
y = 0
print(x and y)
print(x or y)
print(not x)
print(not y)
Output
0
1
False
True

# Q.06-01 Program to arrange two numbers in ascending order

a = int(input())
b = int(input())

if a < b:
    print(a, b)
else:
    print(b, a)

# Q.07-01 Program using compound conditional expression

ans = int(input())

if ans == 0 or ans == 1:
    print("Valid input")
else:
    print("Invalid input")

#Program to print prime and composite numbers from 2 to 12

for n in range(2, 13):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "Prime")
    else:
        print(n, "Composite")

 #Program to find Armstrong numbers between 100 and 999

for n in range(100, 1000):
    s = 0
    temp = n
    while temp > 0:
        d = temp % 10
        s = s + d ** 3
        temp //= 10
    if s == n:
        print(n)

#Combine two lists using nested loops
l1 = ["a", "b", "c"]
l2 = ["1", "2", "3"]

for i in l1:
    for j in l2:
        print(i + j)

#Add new item to dictionary
person = {"Name": "Alex", "Age": 20}
person["Father"] = "John Doe"
print(person)

#Move largest value to last (no temp variable)
lst = [3, 1, 5, 2, 4]

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
      print(lst)

#Convert 2D list to 1D list
a = [[1, 2], [3, 4], [5, 6]]
b = []
for row in a:
    for val in row:
        b.append(val)
print(b)

#Average score from dictionary
maria = {"korean": 90, "english": 88, "math": 89}
avg = sum(maria.values()) / len(maria)
print(avg)

#deepcopy nested dictionary
import copy
school = {"A": {"students": 30}}
school2 = copy.deepcopy(school)
print(school is school2)

# Program to calculate average math score using zip

scores = (
    ("Hyun", 88, 95, 90),
    ("Kang", 78, 85, 80),
    ("Park", 92, 90, 88),
    ("Hong", 85, 89, 91)
)
names, english, math, science = zip(*scores)
avg = sum(math) / len(math)
print(avg)






































































