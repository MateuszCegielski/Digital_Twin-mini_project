"""This is an optional module that can be used to generate sample data for the project"""
import json
import pandas as pd
import numpy as np

if __name__ == "__main__":
    NUMBER_OF_SAMPLE = 20
    C = 760_000

    with open("dataset.csv", "w", encoding="utf-8") as file:
        P = np.random.uniform(76_000, 1_520_000, NUMBER_OF_SAMPLE)
        torque = np.random.uniform(300, 6000, NUMBER_OF_SAMPLE)
        data = pd.DataFrame(
            {
                "P": P,
                "torque": torque
            }
        )

        data.to_csv("dataset.csv", index=False)

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

    with open("data.json", "w", encoding="utf-8") as jsonFile:
        json.dump(dane, jsonFile, indent=4)
