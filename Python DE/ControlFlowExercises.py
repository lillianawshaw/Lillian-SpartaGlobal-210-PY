import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]


i = 0
while i < 5:
    if x[i] % 2 == 0:
        print(x[i])
        i = i + 1
# A1c:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
My_List = []
for i in names:
    My_List.append(i[0])

print(My_List)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:




print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

My_List = []
Space_List = []
Inital_List = []
for i in names:
    My_List.append(i[0])
    Space_List.append(i.find(" "))
    Inital_List.append(i[0] + " " + i[(1 + i.find(" "))])  # (1 + Space_List[i])
print(My_List)
print(Space_List)
print(Inital_List)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates

list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

nonset_list = []

for i in list_of_lists:
    MySet = set(i)
    if len(MySet) == len(i):
        nonset_list.append(MySet)

print(nonset_list)

def CheckUniquieness(a):
    for i in a:
        if a.count(i) > 1:
            return 0


New_List = []

for b in list_of_lists:
    if CheckUniquieness(b) != 0:
        New_List.append(b)

print(New_List)

# another way


# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
while 0 == 0:
    a = input("Please enter a number bigger than 100 ")
    if int(a) < 100:
        print("Please enter a bigger number")
    else:
        print(a)
        break

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

while 0 == 0:
    a = int(input("Please enter a number bigger than 100 "))
    i = 2
    while i < a:
        if a % i == 0 and i != 2:
            print("Not Prime")
            i = i + 1
        i = i + 1
    print("Prime")
# A4b:





