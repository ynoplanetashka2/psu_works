import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

selected_reg = sys.argv[1] if len(sys.argv) > 1 else None

def merge_region_data(data1, data2):
    result = [item1 if item2 == '-' else item2 for (item1, item2) in zip(data1, data2)]
    return result

def standartize(data):
    return (data - np.mean(data)) / np.std(data)

with open('квартиры.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    next(reader)
    result  = []
    for row in reader:
        row = [val.strip() for val in row]
        #primary_housing_market = 0
        #secondary_housing_market = 1
        primary_or_secondary_housing_market = 0 if row[0] == 'Первичный рынок жилья' else 1
        region = row[1]
#        if selected_reg != None:
            #if region != selected_reg:
                #continue

        records = [float(val.replace(' ', '')) if val != '' else '-' for val in row[3:]]
        if '-' in records:
            continue

        result.append({
            'primary_or_secondary': primary_or_secondary_housing_market, 
            'region': region, 
            'records': records
        })

    result2 = []
    extra_indexes = []
    for index, item in enumerate(result):
        if index in extra_indexes:
            continue

        region = item['region']
        for index2, item2 in enumerate(result[index:]):
            region2 = item2['region']
            if region == region2:
                data = item['records']
                data2 = item2['records']
                item['records'] = merge_region_data(data, data2)
                extra_indexes.append(index2)
    result = [item for (index, item) in enumerate(result) if not index in extra_indexes]
    for index, item in enumerate(result):
        item['region'] = index

    #item = next(filter(lambda item: item['region'] == 'Сибирский федеральный округ', result))
    #print(item)

    dates_count = 22 * 4 + 1
    dates = np.linspace(2000.0, 2021.0, dates_count)
    dates = standartize(dates)
    regions_count = len(result)
    regions = np.arange(regions_count)
    regions = standartize(regions)
    housing_market = np.array([item['primary_or_secondary'] for item in result])
    housing_market = standartize(housing_market)
    housing_market_count = housing_market.size

    traits_count = 3
    samples_count = dates_count * regions_count

    X = np.empty((traits_count + 1, samples_count), float)
    Y = np.empty(samples_count, float)

    index = 0
    for item_index, item in enumerate(result):
        region = regions[item_index] 
        housing_market_v = housing_market[item_index]
        records = item['records']

        for date_index, date in enumerate(dates):
            record = records[date_index]
            X[:, index] = [1, date, region, housing_market_v]
            Y[index] = record
            index += 1

    res_4_param = np.matmul(np.linalg.pinv(X).transpose(), Y)
    print(res_4_param)
    poly = lambda x1, x2, x3: res_4_param[0] + res_4_param[1] * x1 + res_4_param[2] * x2 + res_4_param[3] * x3

    accurate_values = np.empty(samples_count, float)
    approx_values= np.empty(samples_count, float)
    index = 0
    for item_index, item in enumerate(result):
        region = regions[item_index] 
        housing_market_v = housing_market[item_index]
        records = item['records']
        for date_index, date in enumerate(dates):
            record = records[date_index]
            poly_val = poly(date, region, housing_market_v)
            accurate_values[index] = record
            approx_values[index] = poly_val
            index += 1

    print(accurate_values, approx_values, regions)
    print(dates, housing_market)
    print(poly(dates[0], regions[0], housing_market[0]), dates[0], regions[0], housing_market[0])
    print(res_4_param)
    plt.plot(accurate_values, approx_values, 'ro')
    plt.plot(np.arange(70000))
    plt.show()
    quit()

    X = np.empty((2, dates_count), float)
    Y = np.empty(dates_count, float)

    avg_records = np.empty(dates_count, float)
    #print(result)
    for index in range(dates_count):
        #print(result[index]['records'])
        avg_records[index] =  np.mean(list(map(lambda x: x['records'][index], result)))
    #print(avg_records)

    for date_index, date in enumerate(dates):
        records = avg_records
        record = records[date_index]
        X[:, date_index] = (1, date)
        Y[date_index] = record

    res = np.matmul(np.linalg.pinv(X).transpose(), Y)

    approx_val = np.empty(dates_count)
    accurate_val = np.empty(dates_count)
    diff_val = np.empty(dates_count)

    for elem_ind in range(dates_count):
        date = dates[elem_ind]
        poly = lambda x: res[0] + x * res[1]
        poly_val = poly(date)
        record = avg_records[elem_ind]
        diff = poly_val - record
        approx_val[elem_ind] = poly_val
        accurate_val[elem_ind] = record
        diff_val[elem_ind] = diff

    #plt.plot(accurate_val, approx_val)
    #plt.plot(dates, approx_val)
    #plt.plot(dates, accurate_val)
    #plt.plot(dates, diff_val)
    plt.show()
