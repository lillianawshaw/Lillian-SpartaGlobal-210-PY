import json

with open('JsonTest') as j:
    data = json.load(j)

print(data)
print(type(data))

with open('output.json', 'w') as f:
    json.dump(data, f)

test_dict = {"name": "Lillian",
             "age": 27,
             "city" : "New York"}

json_file_test = json.dumps(test_dict)

with open('newjson.json', 'w') as d:
    json.dump(json_file_test, d)

