import json
from ft_maths import convert_range
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

dict_data = {}
lst_coord = []
x_coords = []
y_coords = []
mins = []
maxs = []
datas_len = 0
i = 0

def fill(dic, lst, mins, maxsi, datas_len):
    i = 0

    mins.append(dic[u'features'][i][u'geometry'][u'coordinates'][0])
    mins.append(dic[u'features'][i][u'geometry'][u'coordinates'][1])
    maxs.append(dic[u'features'][i][u'geometry'][u'coordinates'][0])
    maxs.append(dic[u'features'][i][u'geometry'][u'coordinates'][1])
    while i < datas_len:
        tmp = [dic[u'features'][i][u'geometry'][u'coordinates'][0],
              dic[u'features'][i][u'geometry'][u'coordinates'][1]]
        lst.append(tmp)
        if dic[u'features'][i][u'geometry'][u'coordinates'][0] < mins[0]:
            mins[0] = dic[u'features'][i][u'geometry'][u'coordinates'][0]
        if dic[u'features'][i][u'geometry'][u'coordinates'][0] > maxs[0]:
            maxs[0] = dic[u'features'][i][u'geometry'][u'coordinates'][0]
        if dic[u'features'][i][u'geometry'][u'coordinates'][1] < mins[1]:
            mins[1] = dic[u'features'][i][u'geometry'][u'coordinates'][1]
        if dic[u'features'][i][u'geometry'][u'coordinates'][1] > maxs[1]:
            maxs[1] = dic[u'features'][i][u'geometry'][u'coordinates'][1]
        i += 1

"""MAIN"""

with open("cities.geojson", "r") as datas:
    dict_data = json.load(datas)
datas_len = dict_data[u'features'].__len__()
fill(dict_data, lst_coord, mins, maxs, datas_len)
"""
while i < datas_len:
    lst_coord[i][0] = convert_range(lst_coord[i][0], mins[0], maxs[0], 
        50, 450)
    lst_coord[i][1] = convert_range(lst_coord[i][1], mins[1], maxs[1], 
        50, 450)
    i += 1
"""
x_coords = [convert_range(lst_coord[i][0], mins[0], maxs[0], 50, 1000)
    for i in range(0, datas_len)]
y_coords = [convert_range(lst_coord[i][1], mins[1], maxs[1], 50, 800)
    for i in range(0, datas_len)]
image = plt.imread(cbook.get_sample_data('worldmap.jpg'))
plt.scatter(x_coords, y_coords, 1)
plt.show()
