### Python : List - Exercises and Solution (Tutor Joe)
# 1
lst = [1,7,-10,34,2,-8]
print(sum(lst))
# 2
lst = [3,4,5,4,7]
s = 1
for i in lst:
    s *= i
print(s)
# 3
lst = [1,7,10,34,2,8]
print(max(lst))
# 4
lst = [51,7,10,34,2,8]
print(min(lst))
# 5
count = 0
for i in ['abc', 'xyz', 'aba', '1221']:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print(count)
# 6
print(set([1,2,3,7,2,1,5,6,4,8,5,4]))
# 7
print( 'List is Not Empty' if len([34,45,6,5,4,56,7]) > 0 else 'List is Empty')
# 8
lst_1 = [10, 22, 44, 23, 4]
lst_2 = lst_1.copy()
print(lst_2)
# 9
n = 4
text = 'Find the List of Words that are Longer than n from a given List of Words'
print([i for i in text.split(' ') if len(i) > n])
# 10
lst1 = [1,2,3,4,5]
lst2 = [5,6,7,8,9]
check = False
for i in lst1:
    for j in lst2:
        if i == j:
            check = True
print('Lists have at least one common member' if check else 'Lists not have at least one common member')
# 11
print([ j for i,j  in enumerate(["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]) if i not in (0, 4, 5) ])
# 12
print([i for i in [7,32,81,20,25,14,23,27] if i % 2 != 0])
# 13
print(list(set(["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"])))
# or
from random import shuffle
animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
shuffle(animal)
print(animal)
# 14
lst_1 = [i**2 for i in range(1, 30)]
print(lst_1[:5])
print(lst_1[-5:])
# or
l = list()
for i in range(11,25):
	l.append(i**2)
print(l[:5])
print(l[-5:])
# 15
import itertools
print(list(itertools.permutations([1,2,3])))
# 16
lst = ['T','u','t','o','r',' ','J','o','e','s']
text = ''
for i in lst:
    text += i
print(text)
# 17
print([20, 70, 30, 90, 10, 30, 90, 10, 80].index(30))
# 18
lst = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
my_lst = []
for i in lst:
    for j in i:
        my_lst.append(j)
print(my_lst)
# or
import itertools
ori_list = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
merged_list = list(itertools.chain(*ori_list))
print(merged_list)
# 19
print([10, 20, 30, 40] + ["Cat", "Dog", "Lion", "Ponda"])
# 20
import random
print(random.choice(["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]))
# or
print(list(set(["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]))[0])
# 21
lst1 = [8, 8, 12, 12, 8]
lst2 = [8, 8, 8, 12, 12]
lst3 = [1, 8, 8, 12, 12]
count1 = 0
count2 = 0
for i in range(len(lst1)):
     for j, k in zip(lst2, lst3):
          if j == lst1[i]:
              count1 += 1
              lst2.remove(j)
          if k == lst1[i]:
              count2 += 1
              lst3.remove(k)
print('List1 and List2:', count1 == len(lst1))
print('List1 and List3:', count2 == len(lst1))
# 22
lst = list(set([2,4,56,78,4,34,5,8,9]))
lst.sort()
print(lst[1])
# 23
lst = list(set([82,4,56,78,4,34,5,100,9]))
lst.sort(reverse=True)
print(lst[1])
# 24
print(list(set([82, 4, 10, 56, 78, 4, 34, 5, 10, 9])))
# 25
lst = [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]
dicts = {}
for i in list(set(lst)):
    dicts[i] = lst.count(i)
print(dicts)
# 26
n = 10
result = [j + str(i) for i in range(1, n + 1) for j in ['T', 'J']]
print(result)
# 27
x = 30
s = "Tutor Joes"
print(format(id(x), 'x'))
print(format(id(s), 'x'))
# 28
lst1 = [23,45,67,78,89,34]
lst2 = [34,89,55,56,39,67]
print(set(lst1) & set(lst2))
# 29
lst = ["cat", "dog", "cow", "tiger", "lion", "Fox", "Shark", "Snake", "turtle", "mouse", "monkey", "bear"]
f_lst = list({i[0] for i in lst})
f_lst.sort()
for i in f_lst:
    print(i)
    for j in lst:
        if i == j[0]:
            print('  ', j)
# 30
print([i for i in [1,2,4,3,6,7,5,8,9,7,8,9,10] if i % 2 != 0])