print("\nQ1a\n")
# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class Country:
    def __init__(self, name, continent, climate, language):
        self.name = name
        self.continent = continent
        self.climate = climate
        self.language = language

    def __str__(self):
        return f"Country: {self.name}\nContinent: {self.continent}\nClimate: {self.climate}\nLanguage: {self.language}"

# Create a Country object
country1 = Country("Iran", "(Western) Asia", "Diverse, 11 out of 13 of the worlds climates. Arid to sub-tropical", "Farsi")

# Print the country's details
print(country1)



print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class


class Country:
    def __init__(self, name, continent, climate, language):
        self.name = name
        self.continent = continent
        self.climate = climate
        self.language = language

    def __str__(self):
        return f"Country: {self.name}\nContinent: {self.continent}\nClimate: {self.climate}\nLanguage: {self.language}"

class City(Country):
    def __init__(self, name, continent, climate, language, city_name):
        super().__init__(name, continent, climate, language)
        self.city_name = city_name


    def __str__(self):
        country_info = super().__str__()
        return f"{country_info}\nCity: {self.city_name}"

# Create a City object
#country1 = Country("Iran", "(Western) Asia",
                   #"Diverse, 11 out of 13 of the worlds climates. Arid to sub-tropical", "Farsi")
city1 = City("Iran", "(Western) Asia",
             "Diverse, 11 out of 13 of the worlds climates. Arid to sub-tropical", "Farsi", "Tehran")

# Print the city's details, including country information
print(city1)


# A1b:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False



# A2a:
# primes from the list in loop
prime_numbers = []
for num in list_of_numbers:
    if Number(num).is_prime():
        prime_numbers.append(num)

print(prime_numbers)

print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
#list of numbers from list divisible by 3 and 4
divisible_by_3_and_4 = []
for num in list_of_numbers:
    if Number(num).divisible_by_n(3) and Number(num).divisible_by_n(4):
        divisible_by_3_and_4.append(num)



print(divisible_by_3_and_4)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)

class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude, behaviour, face)

    def encourage(self):
        print(f"The team cheers for {self.name}, starts shouting awesome slogans, and then gets back to work.")


# A3a: see above (uncommented)


# -------------------------------------------------------------------------------------- #








