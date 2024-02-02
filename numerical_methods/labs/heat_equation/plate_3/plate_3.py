import numpy as np
from produce_next_state import produce_next_state
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns
from time import sleep


fig = plt.figure()
data = np.random.rand(10, 10)
data_ref = { 'data': data }
sns.heatmap(data, vmax=.8, square=True)

ITERATIONS_COUNT = 10_000
ITERATIONS_PER_FRAME = 100

def init():
    sns.heatmap(np.zeros((10, 10)), vmax=.8, square=True, cbar=False)

def animate(anim_index):
    cur_state = data_ref['data']
    fut_state = np.zeros((10, 10))
    for _ in range(ITERATIONS_PER_FRAME):
        for i in range(1, 10 - 1):
            for j in range(1, 10 - 1):
                fut_state[i][j] = produce_next_state(cur_state, i, j)
                # fut_state[i][j] = np.random.rand()
        cur_state = fut_state

    data_ref['data'] = cur_state
    sns.heatmap(data, vmax=.8, square=True, cbar=False)

def main():
    anim = animation.FuncAnimation(fig, animate, init_func=init, repeat = True, interval=10)
    plt.show()

if __name__ == '__main__':
    main()