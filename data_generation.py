"""Here it is going to generate a sample"""
import random
import json


if __name__ == "__main__":
    number_of_sample = 20
    C = 760_000

    with open("dataset.csv", "w") as file:
        line = "force,torque\n"
        file.write(line)
        for i in range(number_of_sample):
            P = C * (random.randint(10, 200) / 100)  # Parameters P will have randomly from 10% to 200% of C value
            torque = 3_000 * (random.randint(10, 200) / 100)
            line = f"{P},{torque}\n"
            file.write(line)

    dane = {
        "bearings": [
            {
                "id": "b1",
                "C": 760_000
            },
            {
                "id": "b2",
                "C": 760_000
            },
        ],
        "shafts": [
            {
                "id": "s1",
                "d": 35,
                "nominal_stress_MPa": 380
            },
            {
                "id": "s2",
                "d": 30,
                "nominal_stress_MPa": 380
            },
            {
                "id": "s3",
                "d": 40,
                "nominal_stress_MPa": 380
            }

        ]

    }

    jsonString = json.dumps(dane)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
