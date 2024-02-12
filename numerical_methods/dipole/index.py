import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def main():
    fig, ax = plt.subplots()
    # ax.set_frame_on(False)
    (line,) = ax.plot([], [], 'ro')
    x, y = np.meshgrid(np.linspace(0, 100, 100), np.linspace(0, 100, 100))
    # z = np.ones((100, 100))
    z = np.sin(x) * np.sin(y)
    # print(x.shape, y.shape, z.shape)
    mesh = ax.pcolormesh(x, y, z)

    def get_frame(angle):
        x_data = [np.sin(angle), np.sin(angle + np.pi)]
        y_data = [np.cos(angle), np.cos(angle + np.pi)]
        delta_1 = np.array([np.sin(angle), np.cos(angle)])
        delta_2 = np.array([np.sin(angle + np.pi), np.cos(angle + np.pi)])
        line.set_data(x_data, y_data)
        x_grid, y_grid = np.meshgrid(np.linspace(0, 10, 100), np.linspace(0, 10, 100))
        dist_1 = np.sqrt((x_grid - delta_1[0])**2 + (y_grid - delta_1[1])**2)
        dist_2 = np.sqrt((x_grid - delta_2[0])**2 + (y_grid - delta_2[1])**2)
        # field_1 = (angle - dist_1)/
        field = np.sin(angle * dist_1)
        mesh.set_array(field.ravel())
        # mesh = ax.pcolormesh(x_grid, y_grid, temp)
        # print(dir(type(mesh)))

    def init():
        line.set_data([], [])
        ax.set_xlim(-2, 100)
        ax.set_ylim(-2, 100)
        # x_grid = np.arange(100)
        # y_grid = np.arange(100)
        # temp = np.random.random(x_grid.size * y_grid.size).reshape((x_grid.size, y_grid.size))
        # mesh.set_array(temp.ravel())

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