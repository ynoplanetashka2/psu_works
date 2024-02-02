import sys
from matplotlib.axis import Axis
from matplotlib.ticker import PercentFormatter
import json
import numpy as np
import matplotlib.pyplot as plt

local_group_file_name = sys.argv[1]
remote_group_file_name = sys.argv[2]

local_group = json.loads(open(local_group_file_name).read())
remote_group = json.loads(open(remote_group_file_name).read())

def bootstrap(data, sample_size, samples_count):
    data_size = data.size
    result_size = data_size + samples_count
    result = np.empty(result_size)
    result[0:data_size] = data

    for index in range(data_size, result_size):
        sample = np.random.choice(data, sample_size)
        sample_mean = np.mean(sample)
        result[index] = sample_mean

    return result
    

local_immediate_matches = np.array(local_group['immediate_tests']['matches'])
local_delayed_matches = np.array(local_group['delayed_tests']['matches'])
remote_immediate_matches = np.array(remote_group['immediate_tests']['matches'])
remote_delayed_matches = np.array(remote_group['delayed_tests']['matches'])

matches = (local_immediate_matches, remote_immediate_matches, local_delayed_matches, remote_delayed_matches)
means = tuple(map(lambda item: np.mean(item), matches))
stds = tuple(map(lambda item: np.std(item), matches))

bootstrapped = tuple(map(lambda item: bootstrap(item, 10, int(1e4)), matches))
#bootstrapped = tuple(map(lambda item: item / item.max(), bootstrapped))
_, ax = plt.subplots()

bins = np.linspace(8, 20, 13)
ax.hist(bootstrapped[0], bins = bins, alpha = .5, density=True, label='сразу')
ax.hist(bootstrapped[2], bins = bins, alpha = .5, density=True, label='через 10 минут')
ax.legend(loc='upper right')
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
ax.set_title('группа с физ. нагрузками')

_, ax = plt.subplots()
ax.hist(bootstrapped[1], bins = bins, alpha = .5, density=True, label='сразу')
ax.hist(bootstrapped[3], bins = bins, alpha = .5, density=True, label='через 10 минут')
ax.set_title('группа без физ. нагрузок')
ax.legend(loc='upper right')
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1))
#print('immediate_mean=%.2f, delayed_mean=%.2f' % (immediate_mean, delayed_mean))
#print('immediate_std=%.2f, delayed_std=%.2f' % (immediate_std, delayed_std))

#plt1.set_xlabel('количество правильных ответов')
#plt1.set_ylabel('участников')
#plt1.set_title('тестирование проведенное сразу')

#plt2.set_xlabel('количество правильных ответов')
#plt2.set_ylabel('участников')
#plt2.set_title('тестирование проведенное через 10 минут')

#immediate_bootstrapped = bootstrap(immediate_matches, 10, int(1e4))
#delayed_bootstrapped = bootstrap(delayed_matches, 10, int(1e4))
#plt1.hist(immediate_bootstrapped, bins = 10)
#plt2.hist(delayed_bootstrapped, bins=10)
#_, plt2 = plt.subplots()
#plt1.plot(immediate_matches, 'ro')
#plt1.plot(mean_line)

#plt2.hist(immediate_matches, bins = 5, alpha = .5)
#plt2.hist(immediate_errors, bins = 5, alpha = .5)

plt.show()
