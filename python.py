# Odd num Pyramid:
    
row_quant = int(input("How many rows of the pyramid shall we use? "))

results = []
offset = 0
for j in range(row_quant):
    sums = 0
    
    for i in range(j+1):
        sums = sums + (2*(i+offset) + 1)
    
    offset += (j+1)

    results.append(sums)

print(results)    

# Analyzing the pattern, each row's result is (row number)^3 ;)

# --------------------------------------------------------------

# Numbering Letters by the order in the dictionary:  
    
def alphabet_position(text):
    values = ""
    i=1
    for char in text:
        if 96 < ord(char) < 123:
            values= values + str((ord(char)-96))
            if i != len(text):
                values = values + " "
                i += 1

        elif 64 < ord(char) < 91:
            values= values + str((ord(char)-64))
            if i != len(text):
                values = values + " "
                i += 1
        else:
            i += 1
        
    return values

# Best Solution:
    
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

#------------------------------------------------------------------

# Summing the lowest two values of a list of numbers:
    
def sum_two_smallest_numbers(numbers):
    numbers.sort() #The sort() method sorts the elements of a given list in a specific ascending or descending order.
                    #It may take two parameters: reverse = by default False, if True it arranges the list in descending order
                    #                           key = a condition through which make the arrangement, see example in doc
    return numbers[0]+numbers[1]

#Best Solution

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2]) #Sorted does not modify the original list but returns a modified list, against sort that does not return anything but modifies the list directly

#---------------------------------------------------------------------

# Generating a phone number from a list of 10 one-digit numbers like (123) 456-7890

def create_phone_number(n):
    phone = "("
    for i in range(len(n)):
        phone = phone + str(n[i])
        if i == 2:
            phone = phone + ") "
        elif i == 5:
            phone = phone + "-"
        else:
            continue
    return phone

#Best solutions

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    n = ''.join(map(str,n))
    # map(fun, iter) function returns a map object(which is an iterator) of the results after applying the given function "fun" to each item of a given iterable "iter" (list, tuple etc.)
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

#---------------------------------------------------------------------

#Transforming any number to Roman



#---------------------------------------------------------------------

#Transforming any number to Roman

# Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

def rgb(r, g, b):
    return get_hex(r)+get_hex(g)+get_hex(b)

def get_hex(x):
    x = max(0, min(255, x))
    result = hex(x).split('x')[-1]
    if len(result) == 1:
        result = '0' + result
    return result[-2:].upper()

# best solutions

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

#---------------------------------------------------------------------

# Calculating with Functions: 8+5 would be eight(plus(five()))

def zero(operation=None):
    return 0 if operation is None else operation(0)
def one(operation=None):
    return 1 if operation is None else operation(1)
def two(operation=None):
    return 2 if operation is None else operation(2)
def three(operation=None):
    return 3 if operation is None else operation(3)
def four(operation=None):
    return 4 if operation is None else operation(4)
def five(operation=None):
    return 5 if operation is None else operation(5)
def six(operation=None):
    return 6 if operation is None else operation(6)
def seven(operation=None):
    return 7 if operation is None else operation(7)
def eight(operation=None):
    return 8 if operation is None else operation(8)
def nine(operation=None):
    return 9 if operation is None else operation(9)

def plus(r_op):
    return lambda x: x + r_op
def minus(r_op):
    return lambda x: x - r_op
def times(r_op):
    return lambda x: x * r_op
def divided_by(r_op):
    return lambda x: x // r_op

# best solutions

id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x

def identity(a): return a
def zero(f=identity): return f(0)
def one(f=identity): return f(1)
def two(f=identity): return f(2)
def three(f=identity): return f(3)
def four(f=identity): return f(4)
def five(f=identity): return f(5)
def six(f=identity): return f(6)
def seven(f=identity): return f(7)
def eight(f=identity): return f(8)
def nine(f=identity): return f(9)
def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b

#---------------------------------------------------------------------

# Invert names and surnames

def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])

# best solutions: MINE

#---------------------------------------------------------------------

# To Camel Case: transform a string with - or _ to camelCase (first word equal, the others capitalized)

def to_camel_case(text):
    return "".join([
        t[0].upper() + t[1:]
        if i!= 0
        else t
        for i, t in enumerate(text.replace("_", "-").split("-"))
    ])

# best solutions

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

#---------------------------------------------------------------------

#



# best solutions



#---------------------------------------------------------------------

#



# best solutions



#---------------------------------------------------------------------



# best solutions



