import re


def ten_times_abc(string):
    return re.fullmatch('(abc){10}', string)
# Write your code here
