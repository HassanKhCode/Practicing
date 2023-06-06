# dict = {'c1': 'Red',
#         'c2': 'Green',
#         'c3': None,
#         'c4': [],
#         'c5': ""}
# def remove_empty(dict: dict) -> dict:
#     new_dict = {}
#     for key, val in dict.items():
#         if dict[key] == "" or dict[key] == [] or dict[key] == None:
#             continue
#         else:
#             new_dict[key] = val
#     return new_dict
# print(remove_empty(dict))

# dict = [('yellow',1), ('blue', 2), ('yellow',3), ('blue', 4), ('red', 5)]
#
#
# def organize(list: list) -> dict:
#         dict = {}
#         for i in list:
#                 if i[0] not in dict:
#                         dict[i[0]] = []
#                         dict[i[0]].append(i[1])
#                 else:
#                         dict[i[0]].append(i[1])
#
#         return dict
# print(organize(dict)


## Unsolved
dicts = {'Science': [88,89,62,95], 'Language': [77,78,84,80]}

def split(dict: dict) ->list:
    new_list = []
    key_list = []
    for key in dict:
        key_list.append({key})
    return new_list
print(split(dicts))