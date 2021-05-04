import csv
import sys
import re

result = []

with open('../title-basics.tsv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')

    for row in reader:
        title = row['primaryTitle']
        duration = row['runtimeMinutes']
        match = re.fullmatch(r'\d+', duration)
        if not match:
            print(row)
            sys.exit(-1)

        if duration != '\\N':
            duration = int(duration)
            result.append([duration, title])
result.sort()
top = reversed(result[-5:])
# print([title for size, title in top])
print("\n".join(([title for size, title in top])))
