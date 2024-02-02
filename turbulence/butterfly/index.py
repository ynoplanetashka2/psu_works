from matplotlib.ticker import AutoMinorLocator
import yaml
import numpy as np
from matplotlib import pyplot as plt
from helpers.T_formula import T_formula
from helpers.antiderivative_with_zero_boundary import antiderivative_with_zero_boundary

from helpers.epsilon_formula import epsilon_formula
from helpers.eta_formula import eta_formula
from helpers.piecewise_linear_approximation import (
    LinearApproximationArgumentRangeException,
    piecewise_linear_approximation,
)
from helpers.t_grad_formula import t_grad_formula


def get_points_for_powers():
    with open("./measurements/data.yml", "r") as file:
        points_for_power = {}

        content = yaml.load(file, yaml.Loader)
        epsilon_shift_values = content["epsilon_shift"]
        TRANSFORM_MM_TO_M = 1_000
        epsilon_shift_values = dict(
            map(
                lambda section_name: (
                    section_name,
                    float(epsilon_shift_values[section_name]) / TRANSFORM_MM_TO_M - 0.4 * 1e-3,
                ),
                epsilon_shift_values,
            )
        )
        for img_label, img_data in content["images"].items():
            eta_values = []
            t_grad_values = []
            scale_factor = img_data["scale_factor"]
            power = img_data["power"]
            sections = img_data["sections"]
            points_for_power[img_label] = {
                "eta_values": eta_values,
                "t_grad_values": t_grad_values,
                "power": power,
            }
            for section_name, points_ in sections.items():
                epsilon_shift = epsilon_shift_values[section_name]
                epsilon = epsilon_formula(epsilon_shift)
                for point in points_:
                    x_value = point["x"] / scale_factor
                    y_value = point["y"] / scale_factor
                    eta_value = eta_formula(x_value, y_value, power)
                    t_grad_value = t_grad_formula(epsilon, x_value, power)

                    eta_values.append(eta_value)
                    t_grad_values.append(t_grad_value)
        return points_for_power


def compute_total_t_grad_of_eta(points_for_powers):
    total_eta_values = [
        eta_value
        for eta_values in (point["eta_values"] for point in points_for_powers.values())
        for eta_value in eta_values
    ]
    total_t_grad_values = [
        t_grad_value
        for t_grad_values in (
            point["t_grad_values"] for point in points_for_powers.values()
        )
        for t_grad_value in t_grad_values
    ]
    return (total_eta_values, total_t_grad_values)


def plot_temperature_line():
    points_for_powers = get_points_for_powers()
    (total_eta_values, total_t_grad_values) = compute_total_t_grad_of_eta(
        points_for_powers
    )
    antiderivative_values = antiderivative_with_zero_boundary(
        [0, *total_eta_values, 8], [0, *total_t_grad_values, 0]
    )

    fig, ax = plt.subplots(1, 2)

    ax[0].set_title(f"t'")
    ax[0].set_xlabel("eta")
    for points_ in points_for_powers.values():
        eta_values = points_["eta_values"]
        t_grad_values = points_["t_grad_values"]
        power = points_["power"]
        ax[0].scatter(
            eta_values, t_grad_values, label=f"Q = {power:.2f} Вт", marker="^"
        )

    ax[1].set_title(f"t")
    ax[1].set_xlabel("eta")
    # ax[1].scatter(antiderivative_values[0], antiderivative_values[1], marker="^")
    ax[1].plot(antiderivative_values[0], antiderivative_values[1])
    ax[1].xaxis.set_minor_locator(AutoMinorLocator(4))
    ax[1].yaxis.set_minor_locator(AutoMinorLocator(4))
    ax[1].grid()
    ax[1].grid(which="minor", linestyle=":")
    ax[1].set(ylim=(0, 5), xlim=(0, 9))

    # ax[2].set_title(f"T")
    # ax[2].scatter(antiderivative_values[0], antiderivative_values[1])

    ax[0].legend()
    ax[0].xaxis.set_minor_locator(AutoMinorLocator(4))
    ax[0].yaxis.set_minor_locator(AutoMinorLocator(4))
    ax[0].grid()
    ax[0].grid(which="minor", linestyle=":")
    ax[0].set(ylim=(0, 5), xlim=(0, 9))

    fig.savefig(f"plots/temperature_line.png")


def plot_temperature_field():
    POWER_VALUE = 5.18
    points_for_powers = get_points_for_powers()
    (total_eta_values, total_t_grad_values) = compute_total_t_grad_of_eta(
        points_for_powers
    )
    antiderivative_values = antiderivative_with_zero_boundary(
        total_eta_values, total_t_grad_values
    )

    piecewise_linear = piecewise_linear_approximation(
        antiderivative_values[0], antiderivative_values[1]
    )

    x_range = np.linspace(0.1, 3, 700) / 1e3
    y_range = np.linspace(0.2, 2, 700) / 1e3

    temperature_field = np.empty((len(x_range), len(y_range)), float)
    for x_index, x in enumerate(x_range):
        for y_index, y in enumerate(y_range):
            eta_value = eta_formula(x, y, POWER_VALUE)
            try:
                t_value = piecewise_linear(eta_value)
            except LinearApproximationArgumentRangeException:
                t_value = 0
            temperature_field[x_index, y_index] = T_formula(x, t_value, POWER_VALUE)

    # generate 2 2d grids for the x & y bounds
    y, x = np.meshgrid(y_range, x_range)
    # переводим из м в мм
    x, y = 1_000 * x, 1_000 * y

    z = temperature_field
    z_min, z_max = z.max(), z.min()

    fig, ax = plt.subplots()
    c = ax.pcolormesh(x, y[::-1], z[:, ::-1], cmap="hot", vmin=z_min, vmax=z_max)

    # set the limits of the plot to the limits of the data
    ax.axis([x.min(), x.max(), y.min(), y.max()])
    fig.colorbar(c, ax=ax)

    ax.set_title(f"Q = {POWER_VALUE:.2f} Вт")
    ax.set_xlabel(f"x, мм")
    ax.set_ylabel(f"y, мм")

    fig.savefig(f"plots/temperature_heatmap.png")


def main():
    plot_temperature_line()


if __name__ == "__main__":
    main()
