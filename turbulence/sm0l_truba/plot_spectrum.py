from operator import itemgetter

from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator, LogLocator
import numpy as np

from helpers.read_data import get_indicators_data_plain
from utils.autocorrelation import autocorrelation
from utils.fft import fft


def average_energy_fft(data: np.ndarray, parts_count: int):
    fft_value_length = int(np.floor(data.size / parts_count / 2))
    energy_fft_values = []
    fft_total_freq = None
    for divider in range(parts_count):
        lower_bound = fft_value_length * divider
        upper_bound = fft_value_length * (divider + 1)
        sub_data = data[lower_bound:upper_bound]
        (fft_freq, fft_data) = fft(sub_data, 0.1)
        energy_fft_values.append(np.power(fft_data, 2))
        fft_total_freq = fft_freq
    energy_fft_values = np.array(energy_fft_values)
    return (fft_total_freq, energy_fft_values.mean(axis=0))


def plot_spectrum(**kwargs):
    (
        input_data,
        average_energy_fft_data,
        autocorrelation_fft_data,
        label,
        descriptor,
    ) = itemgetter(
        "input_data",
        "average_energy_fft_data",
        "autocorrelation_fft_data",
        "label",
        "descriptor",
    )(
        kwargs
    )
    fig, axs = plt.subplots(1, 1)

    (average_energy_fft_freq, average_energy_fft_values) = average_energy_fft_data
    (
        autocorrelation_fft_data_freq,
        autocorrelation_fft_data_values,
    ) = autocorrelation_fft_data

    autocorrelation_fft_normalization_factor = (
        average_energy_fft_values[-1] / autocorrelation_fft_data_values[-1]
    )

    axs.plot(
        autocorrelation_fft_data_freq,
        autocorrelation_fft_data_values * autocorrelation_fft_normalization_factor,
        label="спектр автокорреляционной функции",
    )
    axs.plot(
        average_energy_fft_freq,
        average_energy_fft_values,
        color="orange",
        label="усредненная спектральная плотность энергии",
    )

    kolmogorov_line_domain = autocorrelation_fft_data_freq[
        int(len(autocorrelation_fft_data_freq) / 40) : -int(
            len(autocorrelation_fft_data_freq) / 5
        )
    ]
    kolmogorov_line_values = (
        np.power(kolmogorov_line_domain, -5 / 3) * average_energy_fft_values[-1] * 10
    )
    axs.plot(
        kolmogorov_line_domain,
        kolmogorov_line_values,
        color="black",
        label="наклон -5/3",
    )

    axs.set_xscale("log")
    axs.set_yscale("log")

    axs.legend()

    axs.xaxis.set_minor_locator(LogLocator(base=10, subs=[2.0, 5.0]))
    axs.yaxis.set_minor_locator(LogLocator(base=10, subs=[2.0, 5.0]))
    axs.grid()
    axs.grid(which="minor", linestyle=":")

    axs.set_xlabel(f"частота, Гц")
    axs.set_ylabel(f"энергия")
    fig.savefig(f"output/spectrum/{descriptor}.png", bbox_inches="tight")


def main():
    for data, label, descriptor in map(
        lambda items: itemgetter("data", "label", "descriptor")(items),
        get_indicators_data_plain(),
    ):
        average_energy_fft_data = average_energy_fft(data, 10)
        autocorrelation_data = autocorrelation(data)
        autocorrelation_fft_data = fft(autocorrelation_data[1], 0.1)

        plot_spectrum(
            input_data=data,
            average_energy_fft_data=average_energy_fft_data,
            autocorrelation_fft_data=autocorrelation_fft_data,
            label=label,
            descriptor=descriptor,
        )


if __name__ == "__main__":
    main()
