# # Part 1
# # 1
def gcd(a: int, b: int):
    c = b if a > b else a
    return [i for i in range(1, c + 1) if a % i == 0 and b % i == 0][-1]
# # 2
def find_all_trues(lst: list):
    return [i for i, j in enumerate(lst) if j]
# # 3
def count_vowels(text: str):
    return sum([1 for i in text.lower() if i in 'aeuio'])
# # 4
def remove_duplicates(lst: list):
    return [ i for i in set(lst)]

# # Part 2 SQL concat_ws
def concat_ws(seperator:str, *args):
    result = ''
    for i in args:
        result += i + seperator
    return result[:len(result) - 1]
print(concat_ws(' ', 'test', 'asads','asf'))
print(concat_ws('|', 'test', 'asads','asf'))
print(concat_ws('*', 'test', 'asads','asf'))