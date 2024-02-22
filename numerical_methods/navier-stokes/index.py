from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt

def main():
    RE = 50
    LINE_NODES_COUNT = 20
    COORD_STEP = 1 / LINE_NODES_COUNT
    TIME_STEP = COORD_STEP**2 / (4 * RE)
    psi_values = np.zeros((LINE_NODES_COUNT, LINE_NODES_COUNT))
    fi_values = np.zeros((LINE_NODES_COUNT, LINE_NODES_COUNT))
    
    def step():
        nonlocal psi_values, fi_values
        pass


    fig, ax = plt.subplots()
    (line,) = ax.plot([], [])
    xdata = []
    ydata = []

    def get_frame(frame):
        xdata.append(frame)
        ydata.append(np.sin(frame))
        line.set_data(xdata, ydata)

    def init():
        line.set_data([], [])
        xdata.clear()
        ydata.clear()
        ax.set_xlim(0, 2 * np.pi)
        ax.set_ylim(-1, 1)

    _anim = FuncAnimation(
        fig,
        get_frame,
        frames=np.linspace(0, 2 * np.pi, 100),
        init_func=init,
        blit=True,
        interval=30,
        repeat=True,
        repeat_delay=1,
    )
    plt.show()


if __name__ == "__main__":
    main()
