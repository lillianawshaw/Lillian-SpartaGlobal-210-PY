def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2

def sum(i):
    Fizz = ''
    Bang = ''
    number = i
    if i % 3 == 0:
        number = ''
        Fizz = 'Fizz '
    if i % 5 == 0:
        number = ''
        Bang = 'Bang'
    return str(number) + str(Fizz) + str(Bang)

def string_add(val):
    i = 0
    print(val)
    if val == '' or val == None:
        val = 0
        return val

    numbers = val.rsplit(",")

    for num in numbers:
        if num.count('\n') > 0:
            print(num)
            newlinenum = num.rsplit('\n')
            for numbers in newlinenum:
                i = i + int(numbers)
        else:
            i = i + int(num)
    return i

def Password(input):
    output = ""
    if len(input) < 8:
        output = output + "Password must be at least 8 characters" + "\n"
    count = 0
    Cap_count = 0
    for char in input:
        if char.isdigit():
            count += 1
        if char.isupper():
            Cap_count += 1
    if count < 2:
        output = output + "Password must have two or more numbers" + "\n"
    if Cap_count < 1:
        output = output + "Password must have one or more capital letters" + "\n"

    return output
