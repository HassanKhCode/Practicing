# flowers = ['Rose', 'Lily', 'Tulip', 'Orchid', 'Carnation']
# color = ['red', 'white', 'blue', 'white', 'pink']
# dict = {}
# for i in range(0, len(flowers)):
#     dict[flowers[i]] = color[i]


# def unique(colors: list[str]) -> list:
#     result = []
#     for val in colors:
#         if val.lower() not in result :
#             result.append(val.lower())
#     return result

# color = ['red', 'white', 'blue', 'white', 'pink']
# color2 = ['red', 'white', 'blue', 'white', 'piAk']
# def same(colors1: list[str], colors2: list[str]) -> list:
#     if len(colors1) >= len(colors2):
#         long_list = colors1
#         short_list = colors2
#     else:
#         long_list = colors2
#         short_list = colors1
#     result = []
#     for val in long_list:
#         if val.lower() in short_list and val.lower() not in result:
#             result.append(val.lower())
#     return result
# print(same(color, color2))

# my_cities = {2008: {'Germany': ['Berlin', 'Munich'],
#                     'France': ['Paris', 'Leon', 'Bordeaux']},
#              2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
#                     'Mexico': ['Tijuana', 'Ecatepec']},
#              2010: {'Germany': ['Berlin', 'Dusseldorf'],
#                     'France': ['Paris', 'Nice', 'bordeaux'],
#                     'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}}
# def nodupecities(visited_cities: dict) -> dict:
#     no_dupe_dict = {}
#     for year in visited_cities:
#         for country in visited_cities[year]:
#             if country not in no_dupe_dict:
#                 no_dupe_dict[country] = []
#             for city in visited_cities[year][country]:
#                 if city not in no_dupe_dict[country]:
#                     no_dupe_dict[country].append(city)
#     return no_dupe_dict
# print(nodupecities(my_cities))


# my_cities = {2008: {'Germany': ['Berlin', 'Munich'],
#                     'France': ['Paris', 'Leon', 'Bordeaux']},
#              2009: {'China': ['Hong Kong', 'Shanghai', 'Beijing'],
#                     'Mexico': ['Tijuana', 'Ecatepec']},
#              2010: {'Germany': ['Berlin', 'Dusseldorf'],
#                     'France': ['Paris', 'Nice', 'bordeaux'],
#                     'Japan': ['Tokyo', 'Toyokawa', 'Yatomi']}}
# def arrange_cities(cities: dict) -> dict:
#     city_dict = {}
#     for year in cities:
#         for country in cities[year]:
#             for city in cities[year][country]:
#                 if city not in city_dict:
#                     city_dict[city] = []
#                 city_dict[city].append(year)
#     return city_dict
# print(arrange_cities(my_cities))

