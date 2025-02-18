# Tutor Joe's (50)
# 1
import textwrap

str1 = 'Tutor Joes'
print(len(str1))

# 2
str2 = 'tutorjoes'
list2 = {}
for i in str2:
    if i in list2.keys(): continue
    list2[i] = str2.count(i)
print(list2)

# 3
str3 = 'tutor joes'
print(str3[0] + str3[1:].replace(str3[0], '@'))

# 4
str4_1 = 'abc'
str4_2 = 'xyz'
print(str4_2[0:2] + str4_1[2:] + " " + str4_1[0:2] + str4_2[2:])

# 5
n = 2
str5 = 'Tutor Joes'
print(str5[:n] + str5[n + 1:])

# 6
str6 = 'Python'
print(str6[-1] + str6[1:-1] + str6[0])

# 7
str7 = 'computer education'
print(str7[::2])

# 8
str8 = 'To change the overall look your document. To change the look available in the gallery'
dict8 = {}
for i in set(str8.split(' ')):
    dict8[i] = str8.count(i)
print(dict8)

# 9
str9 = input('Enter the string: ')
print(str9.upper())
print(str9.lower())

# 10
str10 = input('Enter string: ')
if len(str10) % 4 == 0:
    print(str10[::-1])
else:
    print(str10)

# 11
str11 = input('Enter string: ')
count = 0
index = 0
for i in str11:
    if i.isupper():
        count += 1
    index += 1
    if index == 4 or count == 2:
        break
if count == 2:
    print(str11.upper())
else:
    print(str11)

# 12
str11 = input('Enter string: ')
list11 = list(str11.lower())
uppers = [i for i in str11 if i.isupper()]
uppers.sort()
list11.sort()
for i in uppers:
    index = list11.index(i.lower())
    list11[index] = i
print(list11)

# 13
str13 = "\nTutor \nJoes \nComputer \nEducation\n"
print(str13.replace('\n', ''))

# 14
str14 = 'Tutor Joes Computer Education'
pref = 'Tu'
print(str14.startswith(pref))

# 15
import textwrap

str15 = """Python is an interpreted, object-oriented, high-level programming language
that can be used for a wide variety of applications. Python is a powerful
general-purpose programming language."""
print('Formated text (Width 35)')
print(textwrap.fill(str15, width=35))
print('Formated text (Width 70)')
print(textwrap.fill(str15, width=70))

# 16
str16 = """
	Python is an interpreted, object-oriented programming languages.
	high-level programming language that can be used for a wide variety of applications.
	Python is a powerful general-purpose programming language.
	First developed in the late 1980s by Guido van Rossum.
	Python is open source programming language.
	Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""
print(textwrap.dedent(str16))

# 17
str16 = """
	Python is an interpreted, object-oriented programming languages.
	high-level programming language that can be used for a wide variety of applications.
	Python is a powerful general-purpose programming language.
	First developed in the late 1980s by Guido van Rossum.
	Python is open source programming language.
	Guido van Rossum named it after the BBC Comedy TV series Monty Python’s Flying Circus
"""
str16 = textwrap.dedent(str16)
print(textwrap.indent(str16, '* '))

# 18
str18 = 23.36778
print(round(str18, 2))

# 19


# 20


# 21


# 22


# 23


# 24


# 25


# 26


# 27


# 28


# 29


# 30


# 31


# 32


# 33


# 34


# 35


# 36


# 37


# 38


# 39


# 40


# 41


# 42


# 43


# 44


# 45


# 46


# 47


# 48


# 49


# 50
