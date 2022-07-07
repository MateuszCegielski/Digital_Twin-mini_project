""" Here we have two methods to read the data from both file - json and csv """
import csv
import json


def reading_csv(path):
    """Reading data from csv files """
    with open(path, encoding="utf-8") as csv_file:
        csvreader = csv.reader(csv_file)
        header = next(csvreader)
        print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)

    for i in range(len(rows)):
        for j in range(len(rows[0])):
            rows[i][j] = float(rows[i][j])

    return rows


def reading_json(path):
    """Reading data from csv files """
    with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file)
        print(json.dumps(data, indent=1))
    return data