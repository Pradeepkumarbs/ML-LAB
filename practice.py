# 1. Write a program to swap the values of two variables.
a = 10
b = 20
a, b = b, a
print("Swapped values -> a =", a, ", b =", b)


# 2. Write a program to check the largest among the given three numbers.
a = 10
b = 25
c = 15
largest = max(a, b, c)
print("Largest number is:", largest)


# 3. Write a Python program to check if the input year is a leap year or not.
year = int(input("\nEnter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 4. Write a Python program to display the Fibonacci sequence for n terms.
n = int(input("\nEnter number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 5. Write a Python program to print the prime numbers.
n = int(input("\nEnter limit: "))
print("Prime numbers:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()


# 6. Write a function to display the factors of a given number.
def factors(n):
    print("Factors are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

factors(12)


# 7. Write a function to display Fibonacci sequence using recursion.
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("\nEnter terms for recursive Fibonacci: "))
print("Fibonacci (recursion):")
for i in range(n):
    print(fib(i), end=" ")
print()


# 8. Write a function to find the sum of several natural numbers using recursion.
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n-1)

n = int(input("\nEnter n: "))
print("Sum =", sum_n(n))


# 9. Write a program to check whether a string is a palindrome or not.
s = input("\nEnter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 10. Write a program to add two matrices.
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]

print("\nMatrix Addition Result:")
for row in result:
    print(row)


# 11. Write a program to demonstrate string functions.
s = "Hello World"

print("\nString Operations:")
print("Length:", len(s))
print("Index of 'W':", s.index("W"))
print("Slicing:", s[0:5])
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Startswith 'Hello':", s.startswith("Hello"))
print("Endswith 'World':", s.endswith("World"))
print("Concatenation:", s + "!!!")


# 12. Write a program to demonstrate list functions.
list1 = [1, 2, 3]
list2 = [4, 5]

print("\nList Operations:")
print("Concatenation:", list1 + list2)
print("Repetition:", list1 * 2)
print("Slicing:", list1[0:2])
print("Max:", max(list1))
print("Min:", min(list1))

list1.append(6)
print("Append:", list1)

list1.remove(2)
print("Remove:", list1)

list1.sort()
print("Sort:", list1)

list1.reverse()
print("Reverse:", list1)
