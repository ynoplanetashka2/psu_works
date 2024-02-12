import matplotlib.pyplot as plt
from compute_field import compute_field
import numpy as np
from matplotlib.animation import FuncAnimation

def main():
    fig, ax = plt.subplots()
    # (line,) = ax.plot([], [], 'ro')
    x, y = np.meshgrid(np.linspace(0, 100, 100), np.linspace(0, 100, 100))
    z = np.sin(x) * np.sin(y)
    mesh = ax.pcolormesh(x, y, z)

    def get_frame(angle):
        shift = np.array([20, 20])
        charge_1 = np.array([np.sin(angle), np.cos(angle)]) + shift
        charge_2 = np.array([np.sin(angle + np.pi), np.cos(angle + np.pi)]) + shift
        # line.set_data(*zip(charge_1, charge_2))
        fields = []
        for q, position in zip((-1, 1), (charge_1, charge_2)):
            field = compute_field(q, position[0], position[1])
            fields.append(field)
        total_field = fields[0] + fields[1]
        print(fields, total_field.max())
        print(total_field.shape)
        mesh.set_array(total_field.ravel())

    def init():
        # line.set_data([], [])
        ax.set_xlim(-2, 100)
        ax.set_ylim(-2, 100)

    _anim = FuncAnimation(
        fig,
        get_frame,
        frames=np.linspace(0, 2 * np.pi, 100),
        init_func=init,
        interval=30,
        repeat=True,
        repeat_delay=1,
    )
    plt.show()

if __name__ == '__main__':
    main()