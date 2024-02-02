import matplotlib.pyplot as plt
import numpy as np

is_sorted = lambda a: np.all(a[:-1] <= a[1:])

def main():
    with open('./output.txt', 'r') as f:
        lines = f.read().split('\n')
        points = []
        for line in lines:
            if line == '':
                break
            (x, y, z) = map(float, line.split(' '))
            points.append((x, y, z))
        fix, ax =   plt.subplots()
        xgrid = np.sort(
            np.array(list(set(x for (x, y, z) in points)))
        )
        ygrid = np.sort(
            np.array(list(set(y for (x, y, z) in points)))
        )
        grid = list((x, y) for (x, y, z) in points)
        temperature = np.array([z for (x, y, z) in points]).reshape((xgrid.size, ygrid.size))
        print(is_sorted(xgrid))
        print(is_sorted(ygrid))
        # print(temperature)
        # ax.pcolormesh(grid, temperature)
        ax.pcolormesh(xgrid, ygrid, temperature)
        ax.set_frame_on(False)
        plt.show()


if __name__ == '__main__':
    main()
