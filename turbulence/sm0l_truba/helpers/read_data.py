import csv
import os

import numpy as np


def read_csv(filename: str):
    data_array = []
    for i in (0, 1):
        with open(filename) as csvfile:
            spamreader = csv.reader(csvfile, delimiter="\t")
            data = []
            for row in spamreader:
                row = list(
                    map(lambda x: float(x), filter(lambda x: x.lstrip() != "", row))
                )
                data.append(row[i])
            data = np.array(data)
            data_array.append(data)
    return tuple(data_array)


def get_indicators_data():
    for file in os.listdir("./sample"):
        filename = f"./sample/{file}"
        data = read_csv(filename)
        yield (file, data)


def get_indicators_data_plain():
    for file, data in get_indicators_data():
        for i in range(2):
            label = f"file: {file}, indicator index: {i + 1}"
            descriptor = f"{file}_indicator_{i + 1}"
            yield {"data": data[i], "label": label, "descriptor": descriptor}
