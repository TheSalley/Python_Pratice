# coding:utf-8

data = {
    'name': ['alan', 'jack'],
    'age': [18, 22],
    'say': ['hello', 'hi']
}

res = []

keys = list(data.keys())
values = list(data.values())

for length in range(len(list(data.values())[0])):
    obj = dict()
    for key in data.keys():
        obj[str(key)] = ''
    res.append(obj)

for key in data:
    for item in data[key]:
        res[data[key].index(item)][key] = item

print('*****')
print(res)
