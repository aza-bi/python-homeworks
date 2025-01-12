# # 1
# import datetime
# import math
#
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def perimeter(self):
#         return self.r * 2 * math.pi
#
#     def area(self):
#         return self.r ** 2 * math.pi
#
# print(Circle(2).area(), Circle(2).perimeter())
# # 2
# class Person:
#     def __init__(self, n, country, bd):
#         self.n = n
#         self.country = country
#         self.bd = bd
#
#     def persons_age(self):
#         return datetime.date.today().year - int(self.bd.split('.')[2])
#
# print(Person('Aza', 'Uzb', '05.19.2003').persons_age())
# # 3
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def plus(self):
#         return self.a + self.b
#
#     def minus(self):
#         return self.a - self.b
#
#     def multiplications(self):
#         return self.a * self.b
#
#     def division(self):
#         return self.a / self.b
# cal = Calculator(10, 2)
# print(cal.plus(), cal.minus(), cal.multiplications(), cal.division())
# # 4
# class Shape:
#     def __init__(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = self.perimeter() / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#
#     def perimeter(self):
#         return self.r * 2 * math.pi
#
#     def area(self):
#         return self.r ** 2 * math.pi
#
# class Square:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         return 2*(self.a + self.b)
#
#     def area(self):
#         return self.a * self.b
#
# print(Triangle(8, 7, 6).area(), Triangle(8, 7, 6).perimeter())
# print(Circle(8).area(), Circle(8).perimeter())
# print(Square(8, 7).area(), Square(8, 7).perimeter())
# # 5
# class ShoppingCart:
#     def __init__(self):
#         self.chart = []
#
#     def add(self, id, title, price):
#         self.chart.append({'id': id, 'title': title, 'price': price})
#
#     def remove(self, id):
#         for i in self.chart:
#             if i['id'] == id:
#                 self.chart.remove(i)
#                 break
#
#     def calculate_price(self):
#         return sum([i['price'] for i in self.chart])
#
# chart = ShoppingCart()
# chart.add(1, 'Apple', 15000)
# chart.add(2, 'Banana', 30000)
# chart.add(3, 'Orange', 25000)
# chart.add(4, 'Meal', 100000)
# chart.remove(3)
# print(chart.calculate_price())
# # 6
# class Statistics:
#     def __init__(self, data):
#         self.data = data
#
#     def describe(self):
#         return f"""Count: {len(self.data)}
# Sum:  {sum(self.data)}
# Min:  {min(self.data)}
# Max:  {max(self.data)}
# Range:  {max(self.data) - min(self.data)}
# Mean:  {round(sum(self.data)/len(self.data))}
# Median:  {math.floor(sum(self.data)/len(self.data))}
#         """
# print(Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]).describe())
# # 7
# with open('test.txt') as f:
#     content = f.read()
# print(content)
# # 8
# n = 2
# with open('test.txt') as f:
#     content = f.read(n)
# print(content)
# # 9
# text = 'hi'
# with open('test.txt', 'a') as f:
#     f.writelines('\n' + text)
# with open('test.txt', 'r') as f:
#     result = f.read()
# print(result)
# # 10
# n = 3
# with open('test.txt') as f:
#     content = f.read()[int('-'+str(n)):]
# print(content)
# # 11
# with open('test.txt') as f:
#     content = f.readlines()
# print(content)
# # 12


# # 13
# with open('test.txt', 'r') as f:
#     all_text = f.readlines()
#     all_l = []
#     all_w = []
#     for i in all_text:
#         all_l.append(i.replace(',', '').replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace('\n', ''))
#     for i in all_l:
#         for j in i.split(' '):
#             all_w.append(j.lower())
#     result = {}
#     for i in set(all_w):
#         result[i] = all_w.count(i)
#     test = sorted(sorted(result.items()), key=lambda r: r[1], reverse=True)
#     print(dict(test[:10]))
# # 14
# with open('test.txt') as f:
#     text = f.readlines()
# print(len(text))
# # 15
# with open('test.txt', 'r') as f:
#     all_text = f.readlines()
#     all_l = []
#     all_w = []
#     for i in all_text:
#         all_l.append(i.replace(',', '').replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace('\n', ''))
#     for i in all_l:
#         for j in i.split(' '):
#             all_w.append(j.lower())
#     result = {}
#     for i in set(all_w):
#         result[i] = all_w.count(i)
#     test = sorted(sorted(result.items()), key=lambda r: r[1], reverse=True)
#     print(dict(test))
# # 16
# import random
#
# with open('test.txt') as f:
#     content = f.read()
# with open('test-copy.txt', 'w') as f:
#     f.write(content)
# # 17
# with open('test.txt') as f:
#     test = f.readlines()
# print(test[round(random.random() * (len(test)))])
# # 18
# file = 'test.csv'
# with open(file, 'r') as f:
#     all_text = f.readlines()
#     all_l = []
#     all_w = []
#     for i in all_text:
#         all_l.append(i.replace(',', ' ').replace('.', '').replace('!', '').replace('--', '').replace('*', '').replace('\n', ''))
#     for i in all_l:
#         for j in i.split(' '):
#             if j != '':
#                 all_w.append(j.lower())
#     result = {}
#     for i in set(all_w):
#         result[i] = all_w.count(i)
#     test = sorted(sorted(result.items()), key=lambda r: r[1], reverse=True)
#     print(dict(test))
# # 19
# for i in range(65, 65+26):
#     with open(chr(i) + '.txt', 'w') as f:
#         pass