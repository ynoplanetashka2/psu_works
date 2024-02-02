import cv2 as cv
import matplotlib.patches as patches
from scipy.special import erf
from scipy.stats import t
import math
import numpy as np
import random as rand
import matplotlib.pyplot as plt
from get_samples import get_samples

def rand_sample(distr, sample_size):
    sample = np.empty(sample_size)
    for index in range(sample_size):
        randIndex = rand.randrange(sample_size)
        sample[index] = distr[randIndex]
    return sample

def increase_sample(sample, rand_sample_size, rand_samples_count):
    result_size = sample.size + rand_samples_count
    result = np.empty(result_size)
    result[0:sample.size] = np.copy(sample)
    for index in range(sample.size, result_size):
        _rand_sample = rand_sample(sample, rand_sample_size)
        mean = np.mean(_rand_sample)
        result[index] = mean
    return result

def distinct_p(sample1, sample2):
    size1 = sample1.size
    size2 = sample2.size
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    std1 = np.std(sample1)
    std2 = np.std(sample2)

    S = np.sqrt(std1**2/size1 + std2**2/size2)
    _t = np.abs((mean1 - mean2) / S)
    p = (1 - t.cdf(_t, 2.7))
    return p

def plot_hist(jump_rest, jump_act, sit_rest, sit_act, lazy, bins):
    _, _plt = plt.subplots()
    _plt.hist(jump_rest, bins=8, alpha=.5, label='jump rest')
    _plt.hist(jump_act, bins=8, alpha=.5, label='jump act')
    _plt.hist(sit_rest, bins=8, alpha=.5, label='sit rest')
    _plt.hist(sit_act, bins=8, alpha=.5, label='sit act')
    _plt.hist(lazy, bins=8, alpha=.5, label='lazy')
    _plt.legend(loc='upper left')

def draw_matrix(values):
    fig, ax = plt.subplots()
    ax.matshow(values, cmap=plt.cm.Blues)
    x_max, y_max = values.shape
    for i in range(x_max):
        for j in range(y_max):
            txt = '1' if values[j,i] > .05 else '0'
            ax.text(i, j, txt, va='center', ha='center')
    ax.set_xticklabels(['title', 'jump rest', 'jump act', 'sit-ups rest', 'sit-ups act', 'lazy rest', 'lazy act'], rotation=10)
    ax.set_yticklabels(['title', 'jump rest', 'jump act', 'sit-ups rest', 'sit-ups act', 'lazy rest', 'lazy act'])

    fig, ax = plt.subplots()
    ax.matshow(values, cmap=plt.cm.Blues)
    x_max, y_max = values.shape
    for i in range(x_max):
        for j in range(y_max):
            txt = '{:.1f}'.format(values[j,i] * 100)
            ax.text(i, j, txt, va='center', ha='center')
    ax.set_xticklabels(['title', 'jump rest', 'jump act', 'sit-ups rest', 'sit-ups act', 'lazy rest', 'lazy act'], rotation=10)
    ax.set_yticklabels(['title', 'jump rest', 'jump act', 'sit-ups rest', 'sit-ups act', 'lazy rest', 'lazy act'])

samples = list(get_samples())
samples = list(map(lambda _list: np.array(_list, dtype=float), samples))

size = len(samples)
values = np.empty((size, size))
for x in range(size):
    for y in range(size):
        values[x, y] = distinct_p(samples[x], samples[y])

draw_matrix(values)
#for i in range(len(samples)):
    #samples[i] = increase_sample(samples[i], 10, 10**3)

#plt.imshow(np.empty((0, 0)))
plt.show()
