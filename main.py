""" This file is main file of this project, here we are using most of the method and class.
First, the data is imported, then the object are created and their parameters
are calculated and exported after statistical transformations
"""
import json
from collections import defaultdict

import bearing
import shaft
import utilities

PATH_CSV = "dataset.csv"
PATH_JSON = "data.json"

if __name__ == "__main__":
    values_from_csv = utilities.read_csv(PATH_CSV)
    values_from_json = utilities.read_json(PATH_JSON)

    items = []
    for bearing_item in values_from_json["bearings"]:
        items.append(bearing.Bearing(bearing_item["C"], bearing_item["id"]))
    for shaft_item in values_from_json["shafts"]:
        items.append(shaft.Shaft(shaft_item["nominal_stress[MPa]"],
                                 shaft_item["id"], shaft_item["d[cm]"]))

    final_dict = defaultdict(lambda: [])

    for item in items:
        for line in values_from_csv:
            P, torque = line
            if isinstance(item, shaft.Shaft):
                item.calculate_safety_factor(torque)
                item.create_final_data()
            elif isinstance(item, bearing.Bearing):
                item.calculate_durability(P)
                item.create_final_data()

        final_dict = utilities.add_to_dict(final_dict, item.__class__.__name__, {
            "id": item.item_id,
            "results": item.result
        })

    with open("sample.json", "w", encoding="utf-8") as outfile:
        outfile.write(json.dumps(final_dict, indent=1,))
