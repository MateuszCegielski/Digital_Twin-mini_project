import csv
import json


def reading_csv(path):
    csv_file=open(path)
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

def reading_json(path):
    json_file = open(path)
    data = json.load(json_file)
    print(json.dumps(data, indent=1))
    return data
path_csv = "C:/Users/mateusc/Documents/programy w Py/Rozgrzewka/src/dataset.csv"
path_json = "C:/Users/mateusc/Documents/programy w Py/Rozgrzewka/src/data.json"

test = reading_csv(path_csv)
test2 = reading_json(path_json)
print(test)
print(test2)