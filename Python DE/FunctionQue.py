print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


def divisor(a):
    list = []
    i = 1
    while i < a:
        if a % i == 0:
            list.append(i)
        i = i + 1
    list.append(a)
    return list


print(divisor(884))
# A1a:



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factor(a, b):
    if a == 0 or b == 0:
        return False
    if a == b:
        return True
    if a < b:
        if b % a == 0:
            return True
    elif b < a:
        if a % b == 0:
            return True
    return False


print(factor(13, 13))



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# def alpha():
#     while 0 == 0:
#         val = input("Enter a letter ")
#         if alphabet.count(val) == 1:
#             return 1 + alphabet.index(val)
#
#
# print(alpha())

def alpha(val):
    return alphabet.index(val)

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
name = input("state your name ")
def IDMaker(name):
    num = ""
    for i in name:
        num = num + str(alpha(i.lower()))
    return num

# A2b:
print(IDMaker(name))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)
def password(ID):
    ammount = 0
    for i in [*ID]:
        ammount = ammount + int(i)
    print(ammount)
    return(int(ID) - ammount)
# A2c:
print(password(IDMaker(name)))




# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime(val):
    i = 2
    vall = int(val)
    if vall < 2:
        return False
    if vall % 2 != 0:
        halfval = vall + 1
    else:
        halfval = vall
    check = 0
    while i <= (halfval / 2):
        if vall % i == 0:
            i = i + 1
            check = check + 1
        else:
            i = i + 1
    if check == 0:
        return True
    else:
        return False

print(prime(input("Enter a number")))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit
try:
    print(prime(input("Enter a number")))
except:
    print("Do you know what a number is?")
# A3b:



# -------------------------------------------------------------------------------------- #






