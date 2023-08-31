#DISCLAIMER : THE FOLLOWING QUESTIONS WHERE COMPILED AND SHARED BY SPARTA GLOBAL. THE SOLUTIONS TO THESE QUESTIONS ARE MY OWN
#coding language : python,

print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def find_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Example usage
number = 12 # change or request user input is the same thing (
divisors = find_divisors(number)
print(divisors)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_factor(number, potential_factor):
    if number % potential_factor == 0:
        return True
    return False

# Example usage
num1 = 12 # or request user input for each
num2 = 6

result = is_factor(num1, num2)
print(result)  # This will print True



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def letter_position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    return alphabet.index(letter)

# Ask the user to input a letter
input_letter = input("Enter a letter: ")

try:
    position = letter_position(input_letter) +1
    print(f"The position of '{input_letter}' in the alphabet is {position}.")
except ValueError:
    print("Invalid input. Please enter a single letter from the alphabet.")



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def name_to_id(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    id_number = ""
    for letter in name.lower():
        if letter in alphabet:
            id_number += str(alphabet.index(letter) + 1)
            #ignoring the directions since b is 2 not 1 but same thing

    return id_number

# Ask the user to input a name
input_name = input("Enter a name: ")
id_number = name_to_id(input_name)

if id_number:
    print(f"The ID number for '{input_name}' is {id_number}.")
else:
    print("Invalid input. Please enter a name containing letters only.")


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def id_to_password(id_number):
    try:
        id_int = int(id_number)
    except ValueError:
        return None

    id_sum = sum(int(digit) for digit in id_number)
    password = id_int - id_sum
    return password


# Ask the user to input an ID number
input_id = input("Enter an ID number: ")
password = id_to_password(input_id)

if password is not None:
    print(f"The password for ID '{input_id}' is {password}.")
else:
    print("Invalid input. Please enter a valid ID number.")

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


# Ask the user to input a number
input_number = int(input("Enter a number: "))

if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


# Ask the user to input a number
while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        input_number = int(user_input)
        break
    else:
        print("Invalid input. Please enter a valid number.")

if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")

# -------------------------------------------------------------------------------------- #