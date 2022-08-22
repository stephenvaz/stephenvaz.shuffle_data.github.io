import json

with open('data.json', 'r+') as f:
    # data = json.dump({'name': ['test']}, f)
    # # data['name'].append('test')
    # print(data)
    data = json.load(f)
    print(len(data['episodes']))
    # print(data['name'])
    data['episodes'].append(['test', 'test1', 'test2'])
    f.seek(0)
    json.dump(data, f, indent=4)
