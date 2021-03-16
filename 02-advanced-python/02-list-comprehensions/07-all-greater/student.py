# Write your code here
def all_greater(ns, ms):
    return all([n >= m for m in ms for n in ns])
