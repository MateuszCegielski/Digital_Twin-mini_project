""" Here we find a function, which allows adding new values to existing keys in dictionary."""
import json
import pandas as pd


def add_to_dict(final_dict, key, value):
    """ Here we find a function, which allows adding new values to existing keys in dictionary."""
    final_dict[key].append(value)
    return final_dict


def reading_csv(path):
    """Reading data from csv files """
    with open(path, encoding="utf-8") as csv_file:
        data = pd.read_csv(csv_file, index_col=False)
        list_data = data.values.tolist()
        return list_data


def reading_json(path):
    """Reading data from csv files """
    with open(path, encoding="utf-8") as json_file:
        data = json.load(json_file)

    return data
