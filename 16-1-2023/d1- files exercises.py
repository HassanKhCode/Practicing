# import os
# import pprint
#
# ab_path = "C:\\Users\hanfa\Desktop\important files\\username-or-email.csv"
#
# def get_csv_meta(path):
#     with open(path) as f:
#         rows = 0
#         cols = 0
#         for line in f:
#             if line.strip():
#                 rows += 1
#                 cols += len(line.split(";")) - 1
#         return {'rows': rows, 'cols': cols}
# def filter_csv(path):
#     ret_dict = {}
#     for root, dirs, files in os.walk(path):
#         for filename in files:
#             _, ext = os.path.splitext(filename)
#             if ext == ".csv":
#                 full_path = os.path.join(root, filename)
#                 ret_dict[full_path] = get_csv_meta(full_path)
#     return ret_dict
#
#
# if __name__ == '__main__':
#     pprint.pprint(filter_csv("C:\\Users\hanfa\Desktop\important files"))
# import csv
#
# path = "C:\\Users\hanfa\PycharmProjects\Practicing\AAPL.csv"
# new_dict = [{'1980':{'year': '1980',
#                               'Avg_price': 0,
#                               'Min_price': 10,
#                               'Max_price': 0,
#                               'Avg_volume': 0,
#                               'Min_volume': None,
#                               'Max_volume': None}}]
# with open(path) as f:
#     reader = csv.DictReader(f)
#     cnt = 0
#     i = 0
#     total_iterations = 0
#     year2 = '1980'
#     for row in reader:
#         year = str(row['Date'].split("-")[2])
#         if year == new_dict[i][year2]['year']:
#             cnt += 1
#             new_dict[i][year]['Avg_price'] += (float(row['Open']) + float(row['Close'])) / 2
#             if float(row['Low']) < float(new_dict[i][year]['Min_price']):
#                 new_dict[i][year]['Min_price'] = row["Low"]
#             if float(row['High']) > float(new_dict[i][year]['Max_price']):
#                 new_dict[i][year]['Max_price'] = row["High"]
#             if new_dict[i][year]['Min_volume'] == None:
#                 new_dict[i][year]['Min_volume'] = row['Volume']
#             if new_dict[i][year]['Max_volume'] == None:
#                 new_dict[i][year]['Max_volume'] = row['Volume']
#             if float(row['Volume']) < float(new_dict[i][year]['Min_volume']):
#                 new_dict[i][year]['Min_volume'] = row['Volume']
#             if float(row['Volume']) > float(new_dict[i][year]['Max_volume']):
#                 new_dict[i][year]['Max_volume'] = row['Volume']
#             new_dict[i][year]['Avg_volume'] += float(row['Volume'])
#             year2 = year
#             total_iterations += 1
#         else:
#             new_dict[i][year2]['Avg_price'] = new_dict[i][year2]['Avg_price'] / cnt
#             new_dict[i][year2]['Avg_volume'] = new_dict[i][year2]['Avg_volume'] / cnt
#             cnt = 1
#             i += 1
#             new_dict.append(year)
#             new_dict[i] = {year:{'year': year,
#                               'Avg_price': (float(row['Open']) + float(row['Close'])) / 2,
#                               'Min_price': float(row['Low']),
#                               'Max_price': float(row['High']),
#                               'Avg_volume': 0,
#                               'Min_volume': None,
#                               'Max_volume': None}}
#             new_dict[i][year]['Avg_volume'] += float(row['Volume'])
#             if new_dict[i][year]['Min_volume'] == None:
#                 new_dict[i][year]['Min_volume'] = row['Volume']
#             if new_dict[i][year]['Max_volume'] == None:
#                 new_dict[i][year]['Max_volume'] = row['Volume']
#             if float(row['Volume']) < float(new_dict[i][year]['Min_volume']):
#                 new_dict[i][year]['Min_volume'] = row['Volume']
#             if float(row['Volume']) > float(new_dict[i][year]['Max_volume']):
#                 new_dict[i][year]['Max_volume'] = row['Volume']
#             total_iterations += 1
#             year2 = year
#     new_dict[i][year2]['Avg_price'] = new_dict[i][year2]['Avg_price'] / cnt
#     print(new_dict)
#
# year_str = '1980'
# year_int = 1980
# i = 0
# with open("Sum_File.csv", "w") as nf:
#     nf.write("Year,Avg_price,Min_price,Max_price,Avg_volume,Min_volume,Max_volume\n")
#     while year_str != '2023':
#         nf.write(f"{new_dict[i][year_str]['year']},{new_dict[i][year_str]['Avg_price']},{new_dict[i][year_str]['Min_price']},"
#                  f"{new_dict[i][year_str]['Max_price']},{new_dict[i][year_str]['Avg_volume']},{new_dict[i][year_str]['Min_volume']},"
#                  f"{new_dict[i][year_str]['Max_volume']}\n")
#         year_int += 1
#         year_str = str(year_int)
#         i += 1



