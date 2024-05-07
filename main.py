# with open("weather_data.csv") as file:
#     weather_list = file.readlines()
#     print(weather_list)

# with open("weather_data.csv") as file:
#     weather_list = file.read()
#     weather_list = weather_list.split("\n")
#     print(weather_list)


# Using CSV MODULE:
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1].isnumeric():
#             temperature.append(int(row[1]))
#     print(temperature)


# Using PANDAS:
import pandas
#
data = pandas.read_csv("weather_data.csv")
# print(type(data)) #This will return a DATAFRAME, which is forexample the whole data sheet in a excel sheet/csv file
# print("\n\n")
#
# print(type(data["temp"])) # This type is a Series, Like a list of items in the row of the csv file/ excel sheet

# Whole table is DATA FRAME
# Each collumn is a SERIES

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)     USED TO FIND THE AVERAGE:
# print(average)                                                          SUM/NUMBER OF ITEMS

average = data["temp"].mean()     # BUILT IN PANDA FUNCTION
# print(average)                    # DOES THE SAME THING


# CHALLENGE FIND THE MAXIMUM VALUE FOR THE TEMP SERIES USING PANDA DATA SERIES METHODS:

maximum = data["temp"].max()
# print(f"The max value is {maximum}")

# Get data from condition
# Both Function the same
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day =="Monday"])

# CHALLENGE PRINT ROW OF DATA WHERE TEMPERATURE IS THE MAXIMUM
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp.tolist())

# index = df[column_name].index[df[column_name] == element].tolist()[0]
index = data["day"].index[data["day"] == "Monday"].tolist()[0]

day_index = data["day"].get(0)
print(day_index)

# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# gray_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
# cinnamon_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
# black_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
#

#
# gray_len = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# cinnamon_len = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
# black_len = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
#
# print(gray_len)
# print(cinnamon_len)
# print(black_len)
#
# squirrel_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_len, cinnamon_len, black_len]
# }
#
# df = pandas.DataFrame(squirrel_dict)
#
# df.to_csv("Squirrel Color Count")
