"""Here it is going to generate a sample"""
import random
import json


if __name__ == "__main__":
    NUMBER_OF_SAMPLE = 20
    C = 760_000

    with open("dataset.csv", "w",encoding="utf-8") as file:
        LINE = "force,torque\n"
        file.write(LINE)
        for i in range(NUMBER_OF_SAMPLE):
            P = C * (random.randint(10, 200) / 100)
            torque = 3_000 * (random.randint(10, 200) / 100)
            line = f"{P},{torque}\n"
            file.write(line)

    dane = {
        "bearings": [
            {
                "id": "b1",
                "C": 560_000
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
    with open("data.json", "w",encoding="utf-8") as jsonFile:
        jsonFile.write(jsonString)
        jsonFile.close()
