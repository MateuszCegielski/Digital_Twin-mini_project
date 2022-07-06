""" Here we have two methods to read the data from both file - json and csv """
import csv
import json


def reading_csv(path):
    """Reading data from csv files """
    with open(path, encoding="utf-8") as csv_file:
        type(csv_file)
        csvreader= csv.reader(csv_file)
        header = []
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)
    return rows


def reading_json(path,):
    """Reading data from csv files """
    with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=1))
    return data


PATH_CSV = "C:/Users/mateusc/Documents/programy w Py/Rozgrzewka/src/dataset.csv"
PATH_JSON = "C:/Users/mateusc/Documents/programy w Py/Rozgrzewka/src/data.json"

test = reading_csv(PATH_CSV)
test2 = reading_json(PATH_JSON)
print(test)
print(test2)
