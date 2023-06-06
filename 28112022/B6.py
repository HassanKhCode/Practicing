# start = None
# dict = {}
# while start != "quit":
#     start = input("Hey welcome to the birthday dictionary. Do you want to insert a new birthday or lookup one?\
# to quit enter 'quit'\n")
#     if start == "insert" or start == "lookup" or start == "quit":
#         if start == "quit":
#             exit()
#         if start == "insert":
#             name = input("please insert a name:\n")
#             if name in dict:
#                 answer = input("The name is already registered would you like to change the birthday date? Yes/No:\n")
#                 if answer == "Yes" or answer == "yes":
#                     birthday = input("Enter the new birthday: ")
#                     dict[name] = birthday
#                     continue
#                 else:
#                     continue
#             birthday = input("please insert a birthday date:\n")
#             print("Done!")
#             dict[name] = birthday
#             continue
#         elif start == "lookup":
#             name = input("Who's birthday would you like to look for?\n")
#             if name in dict:
#                 print(f"{name}'s birthday is at: {dict[name]}")
#             else:
#                 print("Error username is not saved!")
#             continue
#     print("Oppsie looks like you miss typed")
#     print("Please type one of these commands: 'insert', 'lookup' 'quit'")

# stocks_data = {}
# start = input("To add stock data enter 'add'\
# to search for data enter 'search'\
# to quit enter 'quit':\n")
# while start != "quit":
#     if start == "add":
#         ticker = str(input("Enter the ticker:\n"))
#         if ticker in dict:
#             change = input("This company is already registered would you like to change it?\
#                            type Yes/No")
#             if change == "Yes" or change == "yes":
#                 stocks_data[ticker] = {}
#                 company = input("Enter name:\n")
#                 employees_number = input("Enter amount of workers:\n")
#                 Address = input("Enter address:\n")
#                 CEO = input("Enter name of the CEO:\n")
#                 stocks_data[ticker]['company'] = company
#                 stocks_data[ticker]['employees_number'] = employees_number
#                 stocks_data[ticker]['Address'] = Address
#                 stocks_data[ticker]['CEO'] = CEO
#                 stock_price = {}
#                 date = input("Enter the stock data's date:\n")
#                 open = input("Enter open price:\n")
#                 close = input("Enter close price:\n")
#                 volume = input("Enter Volume:\n")
#                 stock_price[date] = {'open': open,
#                                'close': close,
#                                'volume': volume}
#                 stocks_data[ticker]['stock_price'] = stock_price
#             else:
#                 continue
#     elif start == "search":
#         ticker = input("Enter company's Ticker:\n")
#         if ticker in stocks_data:
#             print(stocks_data[ticker])
#         else:
#             print("This company hasn't registered yet!")
#     start = input("would you like to add/search or quit?\n")
