import json

# with open('descs.json', 'r') as file:
#     a = json.loads(file)

# print(a)

l = [1, 2, 3]
data = {}
data['1'] = l
a = json.dumps(data)
with open('t.json', "w") as file:
    file.write(a)

with open('t.json', 'r') as file:
    a = json.loads(file)

print(a)
