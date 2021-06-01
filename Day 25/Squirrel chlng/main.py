import csv

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)
black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_squirrels_count = len(cinnamon_squirrels)
print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dictionary = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

pandas.DataFrame(data_dictionary).to_csv("squirrel_count.csv")