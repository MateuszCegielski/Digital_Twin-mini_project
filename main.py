import bearing
import shaft
import reading_data

PATH_CSV = "dataset.csv"
PATH_JSON = "data.json"


if __name__ == "__main__":
    values_from_csv = reading_data.reading_csv(PATH_CSV)
    values_from_json = reading_data.reading_json(PATH_JSON)
    # print(values_from_json.items())
    # print(f"To jest csv: {values_from_csv[1]}\n A to z json'a {values_from_json['shafts']} ")
    list_items = []
    for items_group in values_from_json.values():
        for item in items_group:
            if 's' in item['id']:
                list_items.append(shaft.Shaft(item['nominal_stress_MPa'],item["id"],))
                print("To jest shaft")
            elif 'b' in item['id']:
                list_items.append(bearing.Bearing(item["C"],item['id'] ))
            else:
                print("BŁAD")