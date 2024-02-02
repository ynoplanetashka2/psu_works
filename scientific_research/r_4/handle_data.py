import os
import scipy.stats
import matplotlib.pyplot as plt
import sys
import csv
import numpy as np

matches_path = 'matches.csv'
matches_file = open(matches_path, 'r', encoding='utf-8')
subject_frequencies_path = 'subject_frequencies.csv'
subject_frequencies_file = open(subject_frequencies_path, 'r')

csv_matches_reader = csv.reader(matches_file, delimiter=',')
all_ids_matches = next(csv_matches_reader)
all_ids_matches = list(filter(lambda item: item != '', all_ids_matches[1:]))
all_ids_matches = list(map(int, all_ids_matches))
all_ids_matches = np.array(all_ids_matches)
all_ids_matches = all_ids_matches[np.unique(all_ids_matches, return_index=True)[1]]

matches = []
for row in csv_matches_reader:
    freq_range = row[0]
    lower_freq, upper_freq = list(map(int, freq_range.split('-')))
    answers = list(map(lambda x: True if x == 'да' else False, row[1:]))
    matches.append(((lower_freq, upper_freq), answers))



csv_frequencies_reader = csv.reader(subject_frequencies_file, delimiter=',')
subject_frequencies = [list(map(int, row)) for row in csv_frequencies_reader]
subject_frequencies = np.array(subject_frequencies, int)
#subject_frequencies[:, 3] = np.abs(subject_frequencies[:, 3] - subject_frequencies[:, 2])
all_ids_audio = subject_frequencies[np.unique(subject_frequencies[:, 0], return_index=True)[1], 0]
_subject_frequencies = np.empty(subject_frequencies.shape, int)

for index, item_id in enumerate(np.nditer(all_ids_audio)):
    _subject_frequencies[9*index: 9*index+9] = subject_frequencies[subject_frequencies[:,0] == item_id]
subject_frequencies = _subject_frequencies
del _subject_frequencies

all_ids = np.intersect1d(all_ids_audio, all_ids_matches, assume_unique=True)

data_audio = np.empty((all_ids.size, 9), int)
data_test = np.empty(all_ids.size, int)
print(all_ids.size)
#for index, sample_id in enumerate(np.nditer(all_ids)):
    #data_audio[index] = np.int32(np.mean(subject_frequencies[subject_frequencies[:, 0] == sample_id]))

answers = np.empty((all_ids.size, 20), int)
for i in range(all_ids.size):
    for j in range(20):
        lower_freq, upper_freq = matches[j][0]
        is_different = lower_freq != upper_freq
        answer = matches[j][1][i]
        answers[i, j] = 1 if answer != is_different else 0

data_test = np.sum(answers, axis=1)

#for index in np.nditer(np.unique(data_test, return_index=True)[1]):
    #correct_answers_count = data_test[index]
    #_positions = 

for index, item_id in enumerate(np.nditer(all_ids)):
    mask = subject_frequencies[:, 0] == item_id
    dat_audio = subject_frequencies[mask, 3]
    if dat_audio.size < 9:
        print('------')
        print(subject_frequencies[:, 0])
        print(item_id)
        print(mask)
        print(dat_audio)

    data_audio[index] = subject_frequencies[mask, 3]

print(data_audio.shape, data_test.shape)
#ax.boxplot(data_audio[:, ::3].T, positions=data_test)
#ax.set_xlabel('количество правильных ответов')
#ax.set_ylabel('средняя ошибка, Гц')



def standartize(data):
    return (data - np.mean(data)) / np.std(data)

def linreg(data1, data2):
    samples_count = data1.shape[0]
    mat = np.empty((2, samples_count))
    mat[0,:] = np.ones(samples_count)
    mat[1,:] = data1
    return np.matmul(np.linalg.pinv(mat).T, data2)

desired_freq = [261, 330, 440]
#for _i in range(3):
    #data_audio[:, 3*_i:3*(_i+1)] = np.abs(data_audio[:, 3*_i:3*(_i+1)] - desired_freq[_i])


#_, ax = plt.subplots()
#ax.boxplot(data_audio.T, positions=data_test)
#ax.set_xlabel('количество правильных ответов')
#ax.set_ylabel('ошибка в воспроизведении частот, Гц')


#data_audio = data_audio.mean(axis=1)
#print(scipy.stats.pearsonr(data_audio, data_test))

#data_audio = standartize(data_audio)
#data_test = standartize(data_test)

#poly_coef = linreg(data_test, data_audio)
#poly_coef = poly_coef[::-1]
#print(poly_coef)

#
#quit()

#plt.plot(all_ids, np.poly1d(poly_coef)(all_ids))

#plt.show()
#quit()
#
#_, ax = plt.subplots()
#ax.boxplot(data_audio.T)
#ax.set_xlabel('номер добровольца')
#ax.set_ylabel('ошибка в воспроизведении нужной частоты, Гц')
#ax.set_title('все частоты')


#ax.plot(np.arange(1, all_ids.size + 1), np.full(all_ids.size, data_audio.mean(axis=(0, 1))), linestyle='--', label='средняя ошибка')
#ax.legend()
#plt.show()
#print(linreg(np.array([0, 1, 2, 3]), np.array([0, 1.2, 2, 2.9])))
#quit()

for _i in range(3):
    _, ax = plt.subplots()
    data = data_audio[:, 3*_i:3*(_i+1)]
    ax.boxplot(
            data.T,
            #positions=all_ids
    )
    ax.set_title(f'частота: {desired_freq[_i]}')
    ax.set_xlabel('номер добровольца')
    ax.set_ylabel('воспроизводимая частота, Гц')
    ax.plot(
            np.arange(1, all_ids.size + 1, 1),
            np.full(all_ids.size, data.mean(axis=1).mean()), 
            label='средняя воспроизводимая частота', 
            linestyle='--'
    )
    ax.plot(
            np.arange(1, all_ids.size + 1, 1),
            np.full(all_ids.size, desired_freq[_i]), 
            label=f'{desired_freq[_i]}Гц', 
            linestyle='--'
    )
    ax.legend()
    ax.set_yticks(np.arange(0, 760, 31.25), minor=True)
    ax.set_yticks(np.arange(0, 760, 125), minor=False)
    ax.grid(which='both', axis='both')
plt.show()


