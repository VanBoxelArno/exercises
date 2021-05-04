import json
import urllib
import sys

name = sys.argv[1]

with urllib.request.urlopen('https://api.genderize.io/?name=john') as f:
    data = f.read().decode('utf-8')
    data = json.loads(data)
    gender = data['gender']
    prob = round(data['probability'] * 100)
    print(f'{gender}({prob}%)')
