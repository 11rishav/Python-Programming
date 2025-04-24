# write a python program to sort python dictionaries by key or value.
# Sort by Keys:
from yaml import SequenceEndEvent

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))

print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")
# Sort by values
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")


# Write a program that calculates and prints the value according to the given formula:
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a commaseparated sequence.
import math

C = 50
H = 30

def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))

input_sequence = (100, 150, 180)
result = [calculate_Q(D) for D in input_sequence]
print(','.join(map(str, result)))


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
X, Y = 3, 5

array = [[0 for j in range(Y)] for i in range(X)]

for i in range(X):
    for j in range(Y):
        array[i][j] = i * j

for row in array:
    print(row)


# Write a program that accepts a comma separated sequence of words as input and  prints the words in a comma-separated sequence after sorting them alphabetically.
input_sequence = "without, hello, bag, world"
words = input_sequence.split(',')
sorted_words = sorted(words)
sorted_sequence = ','.join(sorted_words)
print("Sorted words:", sorted_sequence)


# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
input_sequence = "hello world and practice makes perfect and hello world again"
words = set(input_sequence.split())
sorted_words = sorted(words)
result = ' '.join(sorted_words)
print("Result:", result)


# Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program:
sentence = "hello world! 123"
letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("LETTERS", letter_count)
print("DIGITS", digit_count)


# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
import re

def is_valid_password(password):
    if 6 <= len(password) <= 12:
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).+$", password):
            return True
    return False

passwords = "ABd1234@1,a F1#,2w3E*,2We3345"
password_list = passwords.split(',')

valid_passwords = []

for psw in password_list:
    if is_valid_password(psw):
        valid_passwords.append(psw)

print(','.join(valid_passwords))


# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class DivisibleBySeven:
    def __init__(self, limit):
        self.limit = limit

    def generate(self):
        for num in range(1, self.limit + 1):
            if num % 7 == 0:
                yield num

n = 50
divisible_by_seven_generator = DivisibleBySeven(n).generate()

for num in divisible_by_seven_generator:
    print(num)



# Write a program to compute the frequency of the words from the input. The output  should output after sorting the key alphanumerically. Suppose the following input is supplied to the program:
input_sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = input_sentence.split()
word_freq = {}
for word in words:
    word = word.strip('.,?')
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
sorted_words = sorted(word_freq.items())
for word, frequency in sorted_words:
    print(f"{word}: {frequency}")


# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"

person = Person()
male = Male()
female = Female()

print(person.getGender())
print(male.getGender())
print(female.getGender())


# Please write a program to generate all sentences where subject is in ["I", "You"] and  verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
sentences = []

for sub in subjects:
    for vrb in verbs:
        for obj in objects:
            sentence = f"{sub} {vrb} {obj}."
            sentences.append(sentence)

for sentence in sentences:
    print(sentence)


# Please write a program to compress and decompress the string "hello world!hello  world!hello world!hello world!".
import zlib
string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(string.encode())
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)


# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 4

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")



# Please write a program using generator to print the numbers which can be divisible  by 5 and 7 between 0 and n in comma separated form while n is input by console.
def divisible_by_5_and_7(n):
    return [i for i in range(1, n+1) if i % 5 == 0 and i % 7 == 0]

try:
    n = 100
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")


# Please write a program using generator to print the even numbers between 0 and n in  comma separated form while n is input by console.
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

try:
    n = 23
    result = even_numbers(n)
    print(','.join(map(str, list(result))))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")


# write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
def fibonacci(n):
 sequence = [0, 1] # Initializing the sequence with the first two F
 [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
 return sequence
try:
 n = 23
 result = fibonacci(n)
 print(','.join(map(str, result)))
except ValueError:
 print("Invalid input. Please enter a valid integer for n.")


# write program to print the user name of a given email address. Both user names and company names are composed of letters only.
def extract_username(email):
    parts = email.split('@')
    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid email format"

try:
    email = "john@google.com"
    username = extract_username(email)
    print(username)
except Exception as e:
    print(f"Error: {e}")


# The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2
shape = Shape()
while True:
    try:
        side_length = float(5)
        if side_length <= 0:
            print("The side length must be a positive number. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
square = Square(side_length)
print("Shape's area by default:", shape.area())
print("Area of the square:", square.area())


# Write a function that stutters a word as if someone is struggling to read it. The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
def stutter(word):
    if len(word) < 2:
        return "Word must be at least two characters long."
    stuttered_word = f"{word[:2]}... {word[:2]}... {word}?"
    return stuttered_word

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))


# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
import math
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)
print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))


# If a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0
print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))


# Given the side length x find the area of a hexagon.
import math
def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x**2) / 2
    return round(area, 1)
print(area_of_hexagon(1))
print(area_of_hexagon(2))
print(area_of_hexagon(3))


# Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number.
def binary(decimal):
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2
    return binary_str if binary_str else "0"
print(binary(1))
print(binary(5))
print(binary(10))


# Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b + 1):
        if num % c == 0:
            total += num
    return total
print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))

# Create a function that returns True if a given inequality expression is correct and False otherwise.
def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False
print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 < 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))


# Create a function that replaces all the vowels in a string with a specified character.
def replace_vowels(string, char):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        string = string.replace(vowel, char)
    return string
print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))


# Write a function that calculates the factorial of a number recursively.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))


# Hamming distance is the number of characters that differ between two strings.
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))


# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
def filter_list(lst):
    result = [ ]
    for element in lst:
        if isinstance(element, int) and element >= 0:
            result.append(element)
    return result

print(filter_list([1, 2, "a", "b"]))

print(filter_list([1, "a", "b", 0, 15]))

print(filter_list([1, 2, "aasf", "1", "123", 123]))


# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
def reverse(input_str):
    reversed_str = input_str[::-1].swapcase()
    return reversed_str

print(reverse("Hello World"))

print(reverse("ReVeRsE"))

print(reverse("Radar"))


# Unpack the list writeyourcodehere into three variables.
writeyourcodehere = [1, 2, 3, 4, 5, 6]
first, *middle, last = writeyourcodehere

print(first)

print(middle)

print(last)


# Write a function that calculates the factorial of a number recursively.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

print(factorial(3))

print(factorial(1))

print(factorial(0))


# Write a function that moves all elements of one type to the end of the list.
def move_to_end(lst, element):

    count = lst.count(element)

    lst = [x for x in lst if x != element]

    lst.extend([element] * count)
    return lst

result = move_to_end([1, 3, 2, 4, 4, 1], 1)
print(result)

print(move_to_end([7,8,9,1,2,3,4],9))

print(move_to_end(["a","a", "a", "b"],"a"))


# A function that takes a string and returns a string and returns a string in which each character is repeated once.
def double_char(input_str):
    doubled_str = ""

    for char in input_str:
        doubled_str += char * 2

    return doubled_str

print(double_char("String"))

print(double_char("Hello World!"))

print(double_char("1234!_ "))


# Create a function that reverses a boolean value and returns the string "boolean  expected" if another variable type is given.
def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"

print(reverse(True))
print(reverse(False))
print(reverse(5))


# Create a function that returns the thickness (in meters) of a piece of paper after folding it n number of times. The paper starts off with a thickness of 0.5mm.
def num_layers(n):
    initial_thickness_mm = 0.5
    final_thickness_mm = initial_thickness_mm * (2 ** n)
    final_thickness_m = final_thickness_mm / 1000
    return f"{final_thickness_m:.3f}m"

print(num_layers(1))

print(num_layers(11))

print(num_layers(23))


# Create a function that takes a single string as argument and returns an ordered list containing the indices of all capital letters in the string.
def index_of_caps(word):
    return [i for i, char in enumerate(word) if char.isupper()]
print(index_of_caps("eDaBiT"))

print(index_of_caps("eQuINoX") )

print(index_of_caps("determine"))

print(index_of_caps("STRIKE"))

print(index_of_caps("sUn"))


# Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
def find_even_nums(num):
    return [x for x in range(1, num + 1) if x % 2 == 0]
print(find_even_nums(8))

print(find_even_nums(11))

print(find_even_nums(23))

print(find_even_nums(50))


# Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]

print(filter_list([1, 2, 3, "a", "b", 4]))

print(filter_list(["A", 0, "Edabit", 1729, "Python", 1729]))

print(filter_list(["Nothing", "here"]))


# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at  index 0, add 1 to the number at index 1, etc...
def add_indexes(lst):
    return [i + val for i, val in enumerate(lst)]
print(add_indexes([0, 0, 0, 0, 0]))

print(add_indexes([1, 2, 3, 4, 5]))

print(add_indexes([5, 4, 3, 2, 1]))


# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
import math
def cone_volume(height, radius):
    if radius == 0:
        return 0
    volume = (1/3) * math.pi * (radius**2) * height
    return round(volume, 2)
print(cone_volume(3, 2))

print(cone_volume(15, 6))

print(cone_volume(18, 0))


# This Triangular Number Sequence is generated from a pattern of dots that form a triangle.
def triangle(n):
    if n < 1:
        return 0
    return n * (n + 1) // 2

print(triangle(1))

print(triangle(6))

print(triangle(215))


# Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
def missing_num(lst):
 total_sum = sum(range(1, 11))
 given_sum = sum(lst)
 missing = total_sum - given_sum
 return missing
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))

print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))

print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))


# Write a function that takes a list and a number as arguments. Add the number to the end of the list, then remove the first element of the list. The function should then  return the updated list.
def next_in_line(lst, num):
    if lst:
        lst.pop(0)
        lst.append(num)
        return lst
    else:
        return "No list has been selected"

print(next_in_line([5, 6, 7, 8, 9], 1))

print(next_in_line([7, 6, 3, 23, 17], 10))

print(next_in_line([1, 10, 20, 42 ], 6))

print(next_in_line([ ], 6))


# Create the function that takes a list of dictionaries and returns the sum of people's budgets.
def get_budgets(lst):
    total_budget = sum(person['budget'] for person in lst)
    return total_budget

budgets1 = [
    {'name': 'John', 'age': 21, 'budget': 23000},
    {'name': 'Steve', 'age': 32, 'budget': 40000},
    {'name': 'Martin', 'age': 16, 'budget': 2700}
]

budgets2 = [
    {'name': 'John', 'age': 21, 'budget': 29000},
    {'name': 'Steve', 'age': 32, 'budget': 32000},
    {'name': 'Martin', 'age': 16, 'budget': 1600}
]

print(get_budgets(budgets1))

print(get_budgets(budgets2))


# Create a function that takes a string and returns a string with its letters in alphabetical order.
def alphabet_soup(txt):
    return ''.join(sorted(txt))

print(alphabet_soup("hello"))

print(alphabet_soup("edabit"))

print(alphabet_soup("geek"))

print(alphabet_soup("hacker"))

print(alphabet_soup("javascript"))


# Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly. What will be the value of your investment at the end of the 10 year period?
# Create a function that accepts the principal p, the term in years t, the interest rate r, and the number of compounding periods per year n. The function returns the value at the end of term rounded to the nearest cent.

def compound_interest(p, t, r, n):
    a = p * (1 + (r / n)) ** (n * t)
    return round(a, 2)
print(compound_interest(10000, 10, 0.06, 12))

print(compound_interest(100, 1, 0.05, 1))

print(compound_interest(3500, 15, 0.1, 4))

print(compound_interest(100000, 20, 0.15, 365))


# Write a function that takes a list of elements and returns only the integers.
def return_only_integer(lst):
    return [x for x in lst if isinstance(x, int)]
print(return_only_integer([9, 2, "space", "car", "lion", 16]))

print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))

print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))

print(return_only_integer(["String", True, 3.3, 1]))


# Create a function that takes three parameters.
def list_operation(x, y, n):

    return [num for num in range(x, y + 1) if num % n == 0]

print(list_operation(1, 10, 3))

print(list_operation(7, 9, 2))

print(list_operation(15, 20, 7))


# Create a function that takes in two lists and returns True if the second list follows the first list by one element, and False otherwise.
def simon_says(list1, list2):

    return list1[:-1] == list2[1:]
print(simon_says([1, 2], [5, 1]))

print(simon_says([1, 2], [5, 5]))

print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))

print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))


# A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order. Create a function that takes in a list of names and returns the name of the secret society.
def society_name(names):
    secret_name = ''.join(sorted([name[0] for name in names]))
    return secret_name

print(society_name(["Adam", "Sarah", "Malcolm"]))

print(society_name(["Harry", "Newt", "Luna", "Cho"]))

print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))

# An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
def is_isogram(word):
    word = word.lower()  # Convert the word to lowercase

    # Create a set to store unique letters in the word
    unique_letters = set()
    for letter in word:
        if letter in unique_letters:
            return False
        unique_letters.add(letter)
    return True
print(is_isogram("Algorism"))

print(is_isogram("PasSword"))

print(is_isogram("Consecutive"))


# Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.
def is_in_order(s):

 return s == ''.join(sorted(s))
print(is_in_order("abc"))

print(is_in_order("edabit"))

print(is_in_order("123"))

print(is_in_order("xyzz"))

# Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical  when it is the same as its reverse.

def is_symmetrical(num):
    num_str = str(num)
    return num_str == num_str[::-1]
print(is_symmetrical(7227))

print(is_symmetrical(12567))

print(is_symmetrical(44444444))

print(is_symmetrical(1112111))


# Given a string of numbers separated by a comma and space, return the product of the numbers.
def multiply_nums(nums_str):

    nums = [int(num) for num in nums_str.split(", ")]

    result = 1

    for num in nums:
        result *= num

    return result

print(multiply_nums("2, 3"))

print(multiply_nums("1, 2, 3, 4"))

print(multiply_nums("54, 75, 453, 0"))

print(multiply_nums("10, -2"))

# Create a function that squares every digit of a number.
def square_digits(n):
    num_str = str(n)

    result_str = ""

    for digit in num_str:

        squared_digit = int(digit) ** 2
        result_str += str(squared_digit)

    return int(result_str)

print(square_digits(9119))

print(square_digits(2483))

print(square_digits(3212))


# Create a function that sorts a list and removes all duplicate items from it.
def setify(lst):
    unique_set = set(sorted(lst))
    return list(unique_set)

print(setify([1, 3, 3, 5, 5]))

print(setify([4, 4, 4, 4]))

print(setify([5, 7, 8, 9, 10, 15]))

print(setify([3, 3, 3, 2, 1]))


# Create a function that returns the mean of all digits.
def mean(n):
    n_str = str(n)
    digit_sum = sum(int(digit) for digit in n_str)
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count
    return int(digit_mean)

print(mean(42))

print(mean(11))

print(mean(12345))

print(mean(666))


# Create a function that takes an integer and returns a list from 1 to the given number
def amplify(num):
    return [n * 10 if n % 4 == 0 else n for n in range(1, num + 1)]

print(amplify(4))

print(amplify(11))

print(amplify(23))

# Create a function that takes a list of numbers and return the number that's unique.
def unique(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num
print(unique([3, 3, 3, 7, 3, 3]))

print(unique([0, 0, 0.77, 0, 0]))

print(unique([0, 1, 1, 1, 1, 1, 1, 1]))


# Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return round(math.pi * self.radius**2)
    def getPerimeter(self):
        return round(2 * math.pi * self.radius)
circy = Circle(11)
print(circy.getArea())
print(circy.getPerimeter())

circy = Circle(4.44)
print(circy.getArea())
print(circy.getPerimeter())


# Create a function that takes a list of strings and return a list, sorted from shortest to longest.
def sort_by_length(lst):
    return sorted(lst, key=len)

print(sort_by_length(["Google", "Apple", "Microsoft"]))

print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))

print(sort_by_length(["Turing", "Einstein", "Jung"]))


# Create a function that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of  the largest number to be validated.
def is_triplet(a, b, c):
    sorted_numbers = sorted([a, b, c])
    return sorted_numbers[0] ** 2 + sorted_numbers[1] ** 2 == sorted_numbers[2] ** 2
print(is_triplet(3, 4, 5))

print(is_triplet(13, 5, 12))

print(is_triplet(1, 2, 3))


# Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
def equal(a, b, c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0
print(equal(3, 4, 3))

print(equal(1, 1, 1) )

print(equal(3, 4, 1))


# Write a function that converts a dictionary into a list of keys-values tuples.
def dict_to_list(input_dict):
    sorted_dict = sorted(input_dict.items())
    result = [(key, value) for key, value in sorted_dict]
    return result

print(dict_to_list({
    "D": 1,
    "B": 2,
    "C": 3
}))

print(dict_to_list({
"likes": 2,
"dislikes": 3,
"followers": 10
}))


# Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
    return result

print(mapping(["p", "s"]))

print(mapping(["a", "b", "c"]))

print(mapping(["a", "v", "y", "z"]))


# Write a function, that replaces all vowels in a string with a specified vowel.
def vow_replace(string, vowel):
    vowels = "aeiou"
    result = ""
    for char in string:
        if char in vowels:
            result += vowel
        else:
            result += char
    return result

print(vow_replace("apples and bananas", "u"))

print(vow_replace("cheese casserole", "o"))

print(vow_replace("stuffed jalapeno poppers", "e"))


# Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
def ascii_capitalize(input_str):
    result = ""

    for char in input_str:
        if ord(char) % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

print(ascii_capitalize("to be or not to be!"))

print(ascii_capitalize("THE LITTLE MERMAID"))

print(ascii_capitalize("Oh what a beautiful morning."))






















































































































































































































































