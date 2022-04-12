import json

f = open('verbes.json')

data = json.load(f)

print(data[3])

f.close()