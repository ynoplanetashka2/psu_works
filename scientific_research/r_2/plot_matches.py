import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import json
import sys
import vectors_to_displacements
from scipy.spatial import distance

def diameter(vectors):
    vectors_count = vectors.shape[0]
    max_dist = 0
    for cur_index in range(vectors_count):
        cur_vec = vectors[cur_index]
        for index in range(cur_index + 1, vectors_count):
            vec = vectors[index]
            dist = distance.euclidean(vec, cur_vec)
            if dist > max_dist:
                max_dist = dist

    return max_dist


input_file_name = sys.argv[1]

output = None
with open(input_file_name, 'r') as file:
    contents = json.loads(file.read())
    distances_count = len(contents)
    hits_count = len(contents[0]['hits'])

    diameters = np.empty(distances_count, int)
    distances = np.fromiter((record['distance'] for record in contents), float)
    _hits = []

    for index, record in enumerate(contents):
        hits = np.array(record['hits'])
        scale_factor = record['scaleFactor']
        rescaled_hits = hits * scale_factor
        diameters[index] = diameter(rescaled_hits)
        #print(rescaled_hits)
        _hits.append(rescaled_hits)

_, ax = plt.subplots()
        
ax.plot(distances, diameters, 'ro', label='экспериментальные данные')
ax.set_xlabel('расстояние выстрела, м')
ax.set_ylabel('величина разброса, мм')

tend_line_poly_coef = np.polyfit(distances, diameters, 2)
tend_line_poly = np.poly1d(tend_line_poly_coef)
tend_line = tend_line_poly(distances)
ax.plot(distances, tend_line, label='аппроксимаиця полиномом 2-го порядка')
ax.set_xticks(np.arange(5, 26, 1), minor=True)
ax.set_xticks(np.arange(5, 26, 3))
ax.set_yticks(np.arange(0, 400, 25), minor=True)
ax.set_yticks(np.arange(0, 400, 50))

plt.grid(which='both')
r, p = scipy.stats.pearsonr(tend_line, diameters)
_err = np.sqrt(np.mean(np.square(diameters - tend_line)))
print(_err)
print(r)

tend_line_poly_coef = np.polyfit(distances, diameters, 1)
tend_line_poly = np.poly1d(tend_line_poly_coef)
tend_line = tend_line_poly(distances)
ax.plot(distances, tend_line, label='аппроксимаиця полиномом 1-го порядка')
r, p = scipy.stats.pearsonr(tend_line, diameters)
_err = np.sqrt(np.mean(np.square(diameters - tend_line)))
print(tend_line_poly_coef)
print(_err)
print(r)

plt.legend()
plt.show()

quit()
_hits = np.array(_hits, dtype=float)
# AHP -> average hit point
avg_hits = np.average(_hits, axis=1)

#print(displacements)
#print('---')
displacements = np.linalg.norm(displacements, axis=2)
displacements = displacements.swapaxes(0, 1)
angles = np.empty(_hits.shape[0:2], float)
#print(displacements)
avg_displ = np.average(displacements, axis=1)
#print(avg_displ.shape)
#print(avg_displ)
_, ax = plt.subplots()

ax.plot(distances, avg_displ, label='avg displacements')
plt.legend()
plt.show()
quit()
for i, records in enumerate(_hits):
    for j, record in enumerate(records):
        avg_hit = avg_hits[i]
        displacement = distance.euclidean(record, avg_hit)
        _distance = distances[i]
        _tan = displacement / _distance
        angles[i, j] = np.arctan(_tan)

for i, records in enumerate(_hits):
    displacements = []
    for j, record in enumerate(records):
        avg_hit = avg_hits[i]
        displacement = distance.euclidean(record, avg_hit)
        displacements.append(displacement)
        _distance = distances[i]
    _, ax = plt.subplots()
    ax.hist(displacements, bins = 4)
    if i > 3:
        break

plt.show()
quit()
avg_angles = np.average(angles, axis = 1)
plt.plot(distances / 25, avg_angles / 0.0045)
plt.show()
quit()

tend_line_poly_coef = np.polyfit(distances, diameters, 2)
tend_line_poly = np.poly1d(tend_line_poly_coef)
tend_line = tend_line_poly(distances)
r, p = scipy.stats.pearsonr(tend_line, diameters)
#print(r, p)
#print(tend_line_poly_coef)

plt.xlabel('СЂР°СЃСЃС‚РѕСЏРЅРёРµ, Рј')
plt.ylabel('СЂР°Р·РјРµСЂ РїРѕРїРµСЂРµС‡РЅРёРєР°, РјРј')

plt.plot(distances, diameters, 'ro', label='СЌРєСЃРїРµСЂРёРјРµРЅС‚Р°Р»СЊРЅС‹Рµ РґР°РЅРЅС‹Рµ')
plt.plot(distances, tend_line, label='Р°РїРїСЂРѕРєСЃРёРјР°С†РёСЏ РїРѕР»РёРЅРѕРјРѕРј 2-РіРѕ РїРѕСЂСЏРґРєР°')
plt.legend()
plt.show()






displacements = (_hits.swapaxes(1, 0) - avg_hits).swapaxes(1, 0)
total_std = np.std(displacements, axis = 1)
total_std = np.linalg.norm(total_std / 2, axis=1)
_, ax = plt.subplots()
ax.plot(distances, total_std, 'ro', label='экспериментальные данные')
ax.set_xlabel('расстояние выстрела, м')
ax.set_ylabel('величина разброса, мм')

tend_line_poly_coef = np.polyfit(distances, total_std, 2)
tend_line_poly = np.poly1d(tend_line_poly_coef)
tend_line = tend_line_poly(distances)
ax.plot(distances, tend_line, label='аппроксимаиця полиномом 2-го порядка')
r, p = scipy.stats.pearsonr(tend_line, total_std)
_err = np.sqrt(np.mean(np.square(total_std - tend_line)))
print(_err)
print(r)

tend_line_poly_coef = np.polyfit(distances, total_std, 1)
tend_line_poly = np.poly1d(tend_line_poly_coef)
tend_line = tend_line_poly(distances)
ax.plot(distances, tend_line, label='аппроксимаиця полиномом 1-го порядка')
r, p = scipy.stats.pearsonr(tend_line, total_std)
_err = np.sqrt(np.mean(np.square(total_std - tend_line)))
print(tend_line_poly_coef)
print(_err)
print(r)

ax.legend()
ax.set_xticks(np.arange(5, 26, 1), minor=True)
ax.set_xticks(np.arange(5, 26, 3))
ax.set_yticks(np.arange(0, 75, 5), minor=True)
ax.set_yticks(np.arange(0, 75, 15))
plt.grid(which='both')
plt.show()
quit()
