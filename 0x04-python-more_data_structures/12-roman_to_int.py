#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [data[val] for val in roman_string] + [0]
    result = 0

    for i in range(len(nums) - 1):
        if nums[i] >= nums[i+1]:
            result += nums[i]
        else:
            result -= nums[i]
    return result
