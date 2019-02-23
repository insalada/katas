#!/usr/bin/env/python3

def add_one(array):
    result = []
    carry = 1
    for n in array[::-1]:
        if n == 9:
            result.insert(0, 0)
            carry = 1
        else:
            result.insert(0, n + carry)
            carry = 0

    if carry > 0 : result.insert(0, 1)
    return result

assert add_one([1, 3, 4]) == [1, 3, 5]
assert add_one([1, 3, 9]) == [1, 4, 0]
assert add_one([1, 9, 9]) == [2, 0, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]