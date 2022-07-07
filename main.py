""" This file is main file of this project, here we are using most of the method and class.
Here the date is imported, then the object are created and their parameters
are calculated and exported after statistical transformations"""
import bearing
import shaft
import reading_data


PATH_CSV = "dataset.csv"
PATH_JSON = "data.json"


if __name__ == "__main__":
    values_from_csv = reading_data.reading_csv(PATH_CSV)
    values_from_json = reading_data.reading_json(PATH_JSON)
    items = []
    for items_group in values_from_json.values():
        for item in items_group:
            if 's' in item['id']:
                items.append(shaft.Shaft(item['nominal_stress_MPa'], item["id"], item["d"], ))
                print("To jest shaft")
            elif 'b' in item['id']:
                items.append(bearing.Bearing(item["C"], item['id']))

            else:
                print("unsupported object".upper())

    for item in items:
        for line in values_from_csv:
            force, torque = line
            if 's' in item.id:
                item.calculate(torque)
                print("To jest shaft")
            elif 'b' in item.id:
                item.calculate(force)
