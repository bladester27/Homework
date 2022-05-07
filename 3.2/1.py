import json

my_dict = {'A': 'a', 'B': 'b', 'C': 'c'}

dict_in_json = json.dumps(my_dict)
with open('output.json', 'w') as f:
    json.dump(my_dict, f)

with open('output.json', 'r') as f:
    my_new_dict = json.load(f)
    print(my_new_dict)
    