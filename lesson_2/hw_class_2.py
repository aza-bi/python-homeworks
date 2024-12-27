# 1
print('Puzzle 1: ')
a = input('Enter number: ')
f = float(a)
i = int(f)

print(str(type(f)) + ': ' + str(f))
print(str(type(i)) + ': ' + str(i))

# 2
print('Puzzle 2: ')
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

print(divmod(a, b))
print(abs(a - b))

# 3
print('Puzzle 3: ')
s = input('Enter the string: ')
l = len(s)
lower = s.lower()

print(l)
print(lower)

# 4 
print('Puzzle 4: ')
base = int(input('Enter the base: '))
exponent = int(input('Enter the exponent: '))
module = int(input('Enter the module: '))

print(pow(base, exponent, module))

# 5 
print('Puzzle 5: ')
print('My name is \t\tAzamat \nAnd you can call me \t\"Aza\"')

# 6 
print('Puzzle 6: ')
s = input('Enter the string: ')

while(len(s) < 3):
    s = input('Enter the string and string must be more than 3 symbols: ')

print('The first symbol: ' + s[0])
print('The third symbol: ' + s[2])
print('The last symbol: ' + s[len(s) - 1])

# 7 
print('Puzzle 7: ')
word = input('Enter string: ')

try: 
    print('This is a int: ' + str(int(word)))
except: 
    try:
        print('This is a float: ' + str(float(word)))
    except:
        print('This is a string: ' + word)

# 8
print('Puzzle 8: ')
string = input('Enter string: ')
try:
    string[1] = '5'
except:
    print('String is a Immutable')

# 9
print('Puzzle 9: ')
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

print('addition is: ' + str(a+b))
print('subtraction is: ' + str(a-b))
print('multiplication is: ' + str(a*b))
print('division  is: ' + str(a/b))
print('integer division is: ' + str(a//b))
print('modulo  is: ' + str(a%b))

# 10
print('Puzzle 10: ')
string = """Hi, my name is Azamat
And now, I'm learning Python"""

print(string)
print(len(string))