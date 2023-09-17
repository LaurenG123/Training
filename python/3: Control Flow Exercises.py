# DISCLAIMER : THE FOLLOWING QUESTIONS WERE COMPILED AND SHARED BY SPARTA GLOBAL. SOLUTIONS TO THESE EXERCISES ARE MY OWN
# coding language : python, run through pycharm

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
first_five_numbers = x[:5]  # so the indicies will span the count 0-4
print(first_five_numbers)

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
even_numbers_from_list = [num for num in x if num % 2 == 0]
# for numbers in list x % used to show is divisible by 2 with no remainder
print(even_numbers_from_list)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
even_numbers_up_to_fifth = [num for num in x[:5] if
                            num % 2 == 0]  # index count starts at 0 therefore ends before 5 (:5) at count 4
print(even_numbers_up_to_fifth)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:


names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
first_initials_of_name = [name.split()[0][0] for name in names]
# for name in names itemises the list
print(first_initials_of_name)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
space_indices = [name.index(" ") for name in names]
print(space_indices)
# note that this gives the character before the space
# remember that the count starts at 0, so if not correct then calculate same but +1


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
initials = [name.split()[0][0] + name.split()[1][0] for name in names]
print(initials)
# use of plus concatenises the string while split reassigns the index of the new initials


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

# A3a:


list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

no_duplicates_lists = [lst for lst in list_of_lists if len(lst) == len(set(lst))]
for lst in no_duplicates_lists:
    print(lst)
# not that using list as a variable name would be wrong since list is already a recognised python command. therefore shortened to lst


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:


while True:
    try:
        number = int(input("Enter a number greater than 100: "))
        if number > 100:
            break
        else:
            print("Number must be greater than 100. Please try again.")
    except ValueError:  # this is used since the input was unexpected therefore yeilding an error
        # at POLITO use of this and try, except is a requirement in code to pass exam
        print("Invalid input. Please enter a valid number.")

print("You entered: ", number)

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

while True:
    try:
        number = int(input("Enter a number greater than 100: "))
        if number > 100:
            break
        else:
            print("Number must be greater than 100. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("You entered: ", number)

# next part (follow on from previous question)
# check if the entered number is prime
# I took this part from a previous university lab i completed while at POLITO

is_it_prime = True
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_it_prime = False
            break

if is_it_prime:
    print("Prime")
else:
    print("Not prime")
