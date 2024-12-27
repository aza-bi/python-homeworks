# sum
def my_sum(nums):
    total = 0
    for i in nums:
        total += i
    print(total)


my_sum([1, 2, 3, 4, 5])


# pow
def my_pow(a, b):
    print(a ** b)


my_pow(10, 2)


# max
def my_max(nums):
    maks = nums[0]
    for i in nums:
        if i > maks:
            maks = i
    print(maks)


my_max([1, 2, 3, 4, 5, 800, 10, 120])


# min
def my_min(nums):
    mini = nums[0]
    for i in nums:
        if mini > i:
            mini = i
    print(mini)


my_min([0, 1, 2, 3, 4, -1])


# len
def my_len(obj):
    count = 0
    for i in obj:
        count += 1
    print(count)


my_len([1, 2, 3, 4, 5])


# zip
def my_zip(*args):
    my_list = []
    for arg in args:
        my_list.append(len(arg))
    mini = min(my_list)
    my_list.clear()
    for i in range(mini):
        for_list = []
        for arg in args:
            for_list.append(arg[i])
        my_list.append(for_list)
    return tuple(my_list)


for i, j, z in my_zip(['test', 'aza'], ['test 3', 'test 4'], ['test_5', 'test_6']):
    print(i, j, z)
for i, j, z in zip(['test', 'aza'], ['test 3', 'test 4'], ['test_5', 'test_6']):
    print(i, j, z)


# enumerate

def my_enumerate(obj: list):
    count = 0
    my_list = []
    for i in obj:
        my_list.append((count, i))
        count += 1
    return tuple(my_list)


for i, j in enumerate(['aza', 'test']):
    print(i, j)
for i, j in my_enumerate(['aza', 'test']):
    print(i, j)


# range
def my_range(a, b=None):
    if b is None:
        b = a
        a = 0

    if b < a:
        return print([])

    my_list = []
    while a < b:
        my_list.append(a)
        a += 1
    print(my_list)


my_range(20)
