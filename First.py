# Write a Python program to print "Hello Python".
print("Hello Python")


# Write a Python program to do arithmetical operations addition and division.
# Addition
num1 = float(5.0)
num2 = float(6.0 )
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# Division
num3 = float(25.0)
num4 = float(5.0)
if num4 == 0:
 print("Error: Division by zero is not allowed.")
else:
 div_result = num3 / num4
 print(f"Division: {num3} / {num4} = {div_result}")


# Write a Python program to find the area of a triangle.
base = float(10)
height = float(15)
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")


# Write a Python program to swap two variables.
a = 5
b = 9
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"Swapped values: a = {a}, b = {b}")


# Write a Python program to generate a random number.
import random
print(f"Random number: {random.randint(1, 100)}")


# Write a Python program to convert kilometers to miles.
kilometers = float(11)
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")


# Write a Python program to convert Celsius to Fahrenheit.
celsius = float(23.0)
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degree celsius is equal to {fahrenheit} degrees fahrenheit")


# Write a Python program to display calendar
import calendar
year = int(2025)
month = int(4)
cal = calendar.month(year, month)
print(cal)


# Write a Python program to solve quadratic equation.
import math
a = float(1)
b = float(4)
c = float(8)
discriminant = b**2 - 4*a*c
if discriminant > 0:
 root1 = (-b + math.sqrt(discriminant)) / (2*a)
 root2 = (-b - math.sqrt(discriminant)) / (2*a)
 print(f"Root 1: {root1}")
 print(f"Root 2: {root2}")
elif discriminant == 0:
 root = -b / (2*a)
 print(f"Root: {root}")
else:
 real_part = -b / (2*a)
 imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
 print(f"Root 1: {real_part} + {imaginary_part}i")
 print(f"Root 2: {real_part} - {imaginary_part}i")



# Write a Python program to swap two variables without temp variable.
a = 5
b = 10
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


# Write a Python Program to Check if a Number is Positive, Negative or Zero.
num = float(23)
if num > 0:
 print("Positive number")
elif num == 0:
 print("Zero")
else:
 print("Negative number")


# Write a Python Program to Check if a Number is Odd or Even.
num = int(23)
if num%2 == 0:
 print("This is a even number")
else:
 print("This is a odd number")


# Write a Python Program to Check Leap Year.
year = int(2025)
if (year % 400 == 0) and (year % 100 == 0):
 print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
 print("{0} is a leap year".format(year))
else:
 print("{0} is not a leap year".format(year))


# Write a Python Program to Check Prime Number.
num = int(23)
# define a flag variable
flag = False
if num == 1:
    print(f"{num} is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")


# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
lower = 1
upper = 23

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# Write a Python Program to Find the Factorial of a Number.
num = int(23)
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'The factorial of {num} is {factorial}')


# Write a Python Program to Display the multiplication Table.
num = int(23)
for i in range(1, 11):
 print(f"{num} X {i} = {num*i}")


# Write a Python Program to Print the Fibonacci sequence.
nterms = int(23)
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# Write a Python Program to Check Armstrong Number?
num = int(153)
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
temp_num = num
while temp_num > 0:
 digit = temp_num % 10
 sum_of_powers += digit ** num_digits
 temp_num //= 10
if sum_of_powers == num:
 print(f"{num} is an Armstrong number.")
else:
 print(f"{num} is not an Armstrong number.")

num = int(23)
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
temp_num = num
while temp_num > 0:
 digit = temp_num % 10
 sum_of_powers += digit ** num_digits
 temp_num //= 10
if sum_of_powers == num:
 print(f"{num} is an Armstrong number.")
else:
 print(f"{num} is not an Armstrong number.")


# Write a Python Program to Find Armstrong Number in an Interval.
lower = int(10)
upper = int(1000)
for num in range(lower, upper + 1):
    order = len(str(num))
    temp_num = num
    sum = 0
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
    if num == sum:
        print(num)


# Write a Python Program to Find the Sum of Natural Numbers.
limit = int(23)
sum = 0
for i in range(1, limit + 1):
 sum += i
print("The sum of natural numbers up to", limit, "is:", sum)


# Write a Python Program to Find LCM.
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(23)
num2 = int(11)
print("The L.C.M. is", compute_lcm(num1, num2))


# Write a Python Program to Find HCF.
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
num1 = int(23)
num2 = int(11)
print("The H.C.F. is", compute_hcf(num1, num2))


# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
dec_num = int(23)
print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")


# Write a Python Program To Find ASCII value of a character.
char = "RISHAV"
print("The ASCII values of the characters in the string are:")

for c in char:
    print(f"The ASCII value of '{c}' is {ord(c)}")


# Write a Python Program to Display Fibonacci Sequence Using Recursion.
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
nterms = int(11)
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))


# Write a Python Program to Find Factorial of Number Using Recursion.
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)
num = int(23)
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# Write a Python Program to calculate your Body Mass Index.
def bodymassindex(height, weight):
 return round((weight / height**2),2)
h = float(1.8)
w = float(70)
print("Welcome to the BMI calculator.")
bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)
if bmi <= 18.5:
 print("You are underweight.")
elif 18.5 < bmi <= 24.9:
 print("Your weight is normal.")
elif 25 < bmi <= 29.29:
 print("You are overweight.")
else:
 print("You are obese.")


# Write a Python Program to calculate the natural logarithm of any number.
import math
num = float(1.4)
if num <= 0:
 print("Please enter a positive number.")
else:
 result = math.log(num)
 print(f"The natural logarithm of {num} is: {result}")


#Write a Python Program to find sum of array.
def sum_of_array(arr):
    total = 0
    for element in arr:
        total += element
    return total
array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array:", result)


# Write a Python Program to find largest element in an array.
def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element

my_array = [10, 20, 30, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")


# Write a Python Program for array rotation.
def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
    return rotated_arr
arr = [1, 2, 3, 4, 5]
d = 2
result = rotate_array(arr, d)
print("Original Array:", arr)
print("Rotated Array:", result)


# Write a Python Program to Split the array and add the first part to the end?
def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    first_part = arr[:k]
    second_part = arr[k:]
    result = second_part + first_part
    return result

arr = [1, 2, 3, 4, 5]
k = 3
result = split_and_add(arr, k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)


# Write a Python Program to check if given array is Monotonic.
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

arr1 = [1, 2, 2, 3]
arr2 = [3, 2, 1]
arr3 = [1, 3, 2, 4]
print("arr1 is monotonic:", is_monotonic(arr1))
print("arr2 is monotonic:", is_monotonic(arr2))
print("arr3 is monotonic:", is_monotonic(arr3))


# Write a Python Program to Add Two Matrices.
def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions"

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = add_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(row)


# Write a Python Program to Multiply Two Matrices.
def multiply_matrices(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if cols1 != rows2:
        return "Matrix multiplication is not possible. Number of columns in the first matrix must equal the number of rows in the second matrix."

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result_matrix = multiply_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)


# Write a Python Program to Transpose a Matrix.
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)


# Write a Python Program to Sort Words in Alphabetic Order.
my_str =  ("suresh ramesh vibhuti gulgule raji ram shyam ajay")
# breakdown the string into a list of words
words = [word.capitalize() for word in my_str.split()]
# sort the list
words.sort()
# display the sorted words
print("The sorted words are:")
for word in words:
 print(word)


# Write a Python Program to Remove Punctuation From a String.
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went"
no_punct = ""

for char in my_str:
    if char not in punctuations:
        no_punct += char

print(no_punct)


# Write a Python program to check if the given number is Happy Number.
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = 1
    return num == 1

num = 23
if is_happy_number(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")


#Write a Python program to determine whether the given number is a Harshad Number.
def is_harshad_number(num):
    digit_sum = 1
    return num % digit_sum == 0
num = 23
if is_harshad_number(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")


# Write a Python program to print all pronic numbers between 1 and 100.
def is_pronic_number(num):
    for n in range(1, int(num**0.5) + 1):
        if n * (n + 1) == num:
            return True
    return False

print("Pronic numbers between 1 and 100 are:")
for i in range(1, 101):
    if is_pronic_number(i):
        print(i, end=" | ")


# Sample list of numbers
numbers = [10, 20, 30, 40, 50]
sum_of_numbers = 0
for i in numbers:
 sum_of_numbers += i
print("Sum of elements in the list:", sum_of_numbers)


# Write a Python program to Multiply all numbers in the list.
numbers = [10, 20, 30, 40, 50]
product_of_numbers = 1
for i in numbers:
    product_of_numbers *= i
print("Product of elements in the list:", product_of_numbers)


# Write a Python program to find smallest number in a list.
numbers = [30, 10, -45, 5, 20]
minimum = numbers[0]
for i in numbers:
    if i < minimum:
        minimum = i
print("The smallest number in the list is:", minimum)


# Write a Python program to find largest number in a list.
numbers = [30, 10, -45, 5, 20]
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print("The largest number in the list is:", maximum)


# Write a Python program to find second largest number in a list.
numbers = [30, 10, 45, 5, 20]

numbers.sort(reverse=True)


if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")


# Write a Python program to find N largest elements from a list.
def find_n_largest_elements(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    # Get the first N elements
    largest_elements = sorted_lst[:n]
    return largest_elements

numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
N = 3
result = find_n_largest_elements(numbers, N)
print(f"The {N} largest elements in the list are:", result)


# Write a Python program to print even numbers in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers in the list:", even_numbers)


# Write a Python program to print odd numbers in a List.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers in the list:", even_numbers)


# Write a Python program to Remove empty List from List.
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in list_of_lists if i]
print("List after removing empty lists:", filtered_list)


# Write a Python program to Cloning or Copying a list.
# 1. Using Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)
# 2. Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)
# 3. Using List Comprehension
original_list = [1, 2, 3, 4, 5]
cloned_list = [item for item in original_list]
print(cloned_list)


# Write a Python program to Count occurrences of an element in a list.
def count_occurrences(l, element):
 count = l.count(element)
 return count

my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list")


# Write a Python program to find words which are greater than given length k.
def find_words(words, k):
    result = [ ]
    for i in words:
        if len(i) > k:
            result.append(i)
    return result  # This should be outside the loop
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")


# Write a Python program for removing ith character from a string.
# def remove_char(input_str, i):
#  if i < 0 or i >= len(input_str):
#   print(f"Invalid index {i}. The string remains unchanged.")
#  return input_str
#
#  result_str = input_str[: i] + input_str[i + 1:]
#  return result_str
#
# input_str = "Hello, wWorld!"
# i = 7
# new_str = remove_char(input_str, i)
#
# print(f"Original String: {input_str}")
# print(f"String after removing {i}th character : {new_str}")


# Write a Python program to split and join a string.
input_str = "Python program to split and join a string"
word_list = input_str.split()
separator = " "
output_str = separator.join(word_list)
print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)


# Write a Python program to check if a given string is binary string or not.
def is_binary_str(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True

input_str = "1001110"
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")


# Write a Python program to find uncommon words from two Strings.
def uncommon_words(str1, str2):
 words1 = set(str1.split())
 words2 = set(str2.split())
 uncommon_words_set = words1.symmetric_difference(words2)
 uncommon_words_list = list(uncommon_words_set)

 return uncommon_words_list

string1 = "This is the first string"
string2 = "This is the second string"
uncommon = uncommon_words(string1, string2)
print("Uncommon words:", uncommon)


# Write a Python program to find all duplicate characters in string.
def find_duplicates(input_str):
    char_count = {}
    duplicates = []
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)

    return duplicates

input_string = "rishav singh"
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters:", duplicate_chars)


# Write a Python Program to check if a string contains any special character.
import re

def check_special_char(in_str):

    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'

    if re.search(pattern, in_str):
        return True
    else:
        return False

input_string = "Hello, World!"
contains_special = check_special_char(input_string)

if contains_special:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")



# Write a Python program to Extract Unique dictionary values.
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}

uni_val = set()
for i in my_dict.values():
 uni_val.add(i)
unique_values_list = list(uni_val)
print("Unique values in the dictionary:", unique_values_list)


# Write a Python program to find the sum of all items in a dictionary.
my_dict = {
 'a': 10,
 'b': 20,
 'c': 30,
 'd': 40,
 'e': 50
}
total_sum = 0
for i in my_dict.values():
 total_sum += i
print("Sum of all items in the dictionary:", total_sum)


# Write a Python program to Merging two Dictionaries.
# 1. Using the update() method:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
# The merged dictionary is now in dict1
print("Merged Dictionary (using update()):", dict1)
# 2. Using dictionary unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary (using dictionary unpacking):", merged_dict)


# Write a Python program to convert key-values list to flat dictionary.
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = {}
for key, value in key_values_list:
 flat_dict[key] = value

print("Flat Dictionary:", flat_dict)


# Write a Python program to insertion at the beginning in OrderedDict.
from collections import OrderedDict

ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
new_item = ('a', 1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)
print("Updated OrderedDict:", new_ordered_dict)


# write a python program to check order of character in string using OrderedDict().
from collections import OrderedDict
def check_order(string, reference):
    string_dict = OrderedDict. fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
    return string_dict == reference_dict

input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string, reference_string) :
    print("The order of characters in the input string matches the  reference string")
else:
    print("The order of characters in the input string does not match the  reference string")



































































































































































































































































































































































































































































































































































































