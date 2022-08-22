import json

f = open('data.json', 'w')
data = json.dump(f)
data['name'].append('testData w/-')
f.close()

f = open('data.json', 'r')

data = json.load(f)

for i in data['name']:
    print(i)

f.close()