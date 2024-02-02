import re
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator, LogLocator
import numpy as np

from helpers.read_data import get_indicators_data
from utils.structure_function import structure_function


def get_structure_functions(first_indicator_values, second_indicator_values):
    myu_values = np.arange(1, 4, 0.5)
    for myu_value in myu_values:
        structure_function_value = structure_function(
            first_indicator_values, second_indicator_values, myu_value
        )

        yield (myu_value, structure_function_value)


def main():
    fig, ax = plt.subplots()
    ax.set_xlabel("l, мм")
    ax.set_ylabel("sum (|T_1 - T_2| ^ q) / N")
    ax.set_title("structure function")
    ax.set_xscale("log")
    ax.set_yscale("log")

    distances_to_points = {}
    distances = []
    myu_values: list[float] | None = None
    for file_name, data in get_indicators_data():
        first_indicator_values = data[0]
        second_indicator_values = data[1]
        distance = re.search(r"^\d+", file_name)
        if distance is None:
            raise Exception("wrong file name")
        distance = int(distance.group())
        distances.append(distance)
        points = [
            point
            for point in get_structure_functions(
                first_indicator_values, second_indicator_values
            )
        ]
        x_values = list(map(lambda a: a[0], points))
        y_values = list(map(lambda a: a[1], points))
        myu_values = x_values
        distances_to_points[distance] = y_values
    if myu_values is None:
        raise Exception("unreachable")

    myu_to_angles = {}
    for myu_index, myu_value in enumerate(myu_values):
        x_values = sorted(distances)
        y_values = [distances_to_points[distance][myu_index] for distance in x_values]
        (angle, _) = np.polyfit(np.log10(x_values[2:]), np.log10(y_values[2:]), 1)
        myu_to_angles[myu_value] = angle
        ax.plot(
            x_values,
            y_values,
            label=f"q = {myu_value:.2f}, тангенциальный угол: {angle:.2f}",
            marker="o",
        )

    ax.legend()

    ax.xaxis.set_minor_locator(LogLocator(base=10, subs=[2.0, 5.0]))
    ax.yaxis.set_minor_locator(LogLocator(base=10, subs=[2.0, 5.0]))
    ax.grid()
    ax.grid(which="minor", linestyle=":")

    fig.savefig(f"output/structure_functions/structure_functions.png")

    fig, ax = plt.subplots()

    myu_values = list(sorted(myu_to_angles))
    angles_values = [myu_to_angles[myu_value] for myu_value in myu_values]

    myu_to_angles_angle = (myu_values[-1] - myu_values[0]) / (
        angles_values[-1] - angles_values[0]
    )
    myu_to_angles_angle = myu_to_angles_angle ** (-1)
    ax.set_xlabel("q")
    ax.set_ylabel("тангенциальный угол")

    ax.plot(
        myu_values,
        angles_values,
        marker="o",
        label=f"зависимость тангенциального угла от q \n (тангенциальный угол графика {myu_to_angles_angle:.2f})",
    )

    ax.legend()

    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    ax.grid()
    ax.grid(which="minor", linestyle=":")

    ax.set_xlim((0.5, 3.6))
    ax.set_ylim((0.5, 2.3))
    fig.savefig(f"output/structure_functions/myu_to_angles.png")


if __name__ == "__main__":
    main()
