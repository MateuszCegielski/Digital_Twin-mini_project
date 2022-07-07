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
            elif 'b' in item['id']:
                items.append(bearing.Bearing(item["C"], item['id']))

            else:
                print("unsupported object".upper())

    for item in items:
        for line in values_from_csv:
            force, torque = line
            if 'shaft'.casefold() == item.__class__.__name__.casefold():
                item.calculate(torque)
                item.creating_final_data()
            elif 'bearing'.casefold() == item.__class__.__name__.casefold():
                item.calculate(force)
                item.creating_final_data()

        print(f"To wyniki z {item.__class__.__name__} : {item.result}")
