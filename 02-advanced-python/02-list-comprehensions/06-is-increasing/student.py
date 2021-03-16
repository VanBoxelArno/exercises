# Write your code here
def is_increasing(ns):
    return all([x <= y for x, y in zip(ns, ns[1:])])
