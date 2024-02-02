from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
from operator import itemgetter

def linear_approximation_least_squares(x_arr, y_arr):
    N = x_arr.shape[0]
    x_mean, y_mean = np.mean(x_arr), np.mean(y_arr)
    S_xx = np.sum((x_arr - x_mean)**2)
    S_xy = np.sum((x_arr - x_mean) * (y_arr - y_mean))
    S_yy = np.sum((y_arr - y_mean)**2)
    
    a = S_xy / S_xx
    b = y_mean - x_mean * a
    c = S_xy / np.sqrt(S_xx * S_yy)
    
    S_e = np.sum((y_arr - (a * x_arr + b))**2)
    R_sq = 1 - S_e / S_yy
    sigma = np.sqrt(S_e / (N - 2))

    y_exp_arr = a * x_arr + b
    y_exp_mean = np.mean(y_exp_arr)
    S_yy_exp = np.sum((y_arr - y_mean) * (y_exp_arr - y_exp_mean))
    S_y_expy_exp = np.sum((y_exp_arr - y_exp_mean)**2)
    
    R = S_yy_exp / np.sqrt(S_yy * S_y_expy_exp)

    output = {'a': a, 'b': b, 'c': c, 'R': R, 'R_sq': R_sq, 'N': N, 'sigma': sigma, 'x_mean': x_mean, 'y_mean': y_mean, 'S_xx': S_xx, 'S_yy': S_yy, 'S_xy': S_xy, 'S_e': S_e, 'S_yy_exp': S_yy_exp, 'S_y_expy_exp': S_y_expy_exp, 'y_exp_mean': y_exp_mean, 'y_exp_arr': y_exp_arr}
    
    return output

def discard_misses(x_arr, y_arr, interval):
    y_mean = np.mean(y_arr)
    filter_mask = np.array(np.absolute(y_arr - y_mean) < interval)
    x_filtered = x_arr[filter_mask]
    y_filtered = y_arr[filter_mask]
    return x_filtered, y_filtered, filter_mask

def get_confidence_interval(alpha, **kwargs):
    f = stats.f.pdf
    N, x_mean, S_xx, S_e = itemgetter('N', 'x_mean', 'S_xx', 'S_e')(kwargs)
    degrees_of_freedom = N - 2
    return lambda x: np.sqrt(f(alpha, 1, degrees_of_freedom) * (1 + 1/N + (x - x_mean)**2 / S_xx) * S_e / (N - 2))

input_file_name = sys.argv[1]
rows_count = None
with open(input_file_name, 'r') as input_file:
    rows_count = max(item[0] for item in enumerate(input_file)) + 1

with open(input_file_name, 'r') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    data = np.empty((rows_count, 2), float)
    data[:] = np.array([np.array([float(coord.replace(',', '.')) for coord in point], float) for point in reader])
    data[:, 0] *= 3.24078e-17
    approx_dict = linear_approximation_least_squares(data[:, 0], data[:, 1])
    y_exp_arr, c = itemgetter('y_exp_arr', 'c')(approx_dict)
    R, R_sq = itemgetter('R', 'R_sq')(approx_dict)
    sigma = itemgetter('sigma')(approx_dict)
    a, b = itemgetter('a', 'b')(approx_dict)
    cleaned_x, cleaned_y, filter_mask  = discard_misses(data[:, 0], data[:, 1], sigma)
    print(a / 3.24078e-17)

    approx_dict = linear_approximation_least_squares(cleaned_x, cleaned_y)
    y_exp_arr, c = itemgetter('y_exp_arr', 'c')(approx_dict)
    R, R_sq = itemgetter('R', 'R_sq')(approx_dict)
    sigma = itemgetter('sigma')(approx_dict)
    a, b = itemgetter('a', 'b')(approx_dict)
    print(a / 3.24078e-17)

    slope, intercept, r_value, p_value, std_err = stats.linregress(data[:, 0], data[: ,1])
    conf_int1 = get_confidence_interval(.05, **approx_dict)
    conf_int2 = get_confidence_interval(.01, **approx_dict)
    approx_line = lambda x: a * x + b
    upper_bound1 = np.array([approx_line(x) + conf_int1(x) for x in cleaned_x])
    lower_bound1 = np.array([approx_line(x) - conf_int1(x) for x in cleaned_x])
    lower_bound2 = np.array([approx_line(x) - conf_int2(x) for x in cleaned_x])
    upper_bound2 = np.array([approx_line(x) + conf_int2(x) for x in cleaned_x])

    dfn, dfd = 1e0, 1e3
    rv = stats.f(dfn, dfd)
    x = [.1, .2, .3, .4, 10]
    #_, ax = plt.subplots()
    #ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

    _, _plt = plt.subplots()
    _plt.plot(cleaned_x, cleaned_y, 'ro')
    _plt.plot(cleaned_x, y_exp_arr, linewidth=6)
    _plt.plot(cleaned_x, upper_bound1, color='yellow')
    _plt.plot(cleaned_x, lower_bound1, color='yellow')
    _plt.plot(cleaned_x, upper_bound2, color='yellow')
    _plt.plot(cleaned_x, lower_bound2, color='yellow')
    _plt.fill_between(cleaned_x, upper_bound1, lower_bound1, color='green', alpha=.3)
    _plt.fill_between(cleaned_x, upper_bound2, lower_bound2, color='gray', alpha=.2)
    plt.show()

