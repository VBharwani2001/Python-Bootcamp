# import csv
# weather_data = []
# with open("./weather_data.csv", "r") as data:
#     detail = csv.reader(data)
#     for row in detail:
#         weather_data.append(row)
#         #print(row)
#
# print(weather_data)

import pandas
data = pandas.read_csv("weather_data.csv")
temperature = data["temp"].to_list()
temperature_average = sum(temperature)/len(temperature)
max_temperature = data["temp"].max()
print(max_temperature)
print(temperature_average)
print(data[data.temp == max_temperature])