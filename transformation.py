#!usr/bin/python3.6

#File that tranforms the data and structures into another form (Data Transformation operations)


import numpy as np



#Function that deletes useless maps
def delete_garbage_maps(array):
    index = 0
    for item in array:
        if item[0] == 'Default' or item[0] == 'Tuscan' or item[0] == 'Season' or item[0] == 'TBA':
            array = np.delete(array, index, 0)
        else:
            index += 1
    return array


#Function that deletes matches if one of the two teams is not interesting
def delete_garbage_dict(dictio, l):
	for i,v in dictio.items():
		if v[9] not in l or v[11] not in l:
			del dictio[v]
	return dictio


#Conversion of Numpy array into dictionary
def numpy_to_dict(array, l):
	dictio = {}
	index = 0
	for item in array:
		if item[1] in l and item[3] in l:
			dictio[index] = [0, 0, 0, 0, 0, 0, 0, 0, item[0], item[1], item[2], item[3], item[4]]
			index += 1
	return dictio


#Encoding of the name of the map into binary value
def map_encoding(dictio):
	for i,v in dictio.items():
		if v[8] == 'Mirage':
			v[0] = 1
		elif v[8] == 'Cache':
			v[1] = 1
		elif v[8] == 'Cobblestone':
			v[2] = 1
		elif v[8] == 'Inferno':
			v[3] = 1
		elif v[8] == 'Train':
			v[4] = 1
		elif v[8] == 'Overpass':
			v[5] = 1
		elif v[8] == 'Dust2':
			v[6] = 1
		elif v[8] == 'Nuke':
			v[7] = 1
	return dictio


#Binary encoding for victory and defeat of team 1 and team 2
def result_encoding(dictio):
	for i,v in dictio.items():
		if v[10] > v[12]:
			v[10] = 1
			v[12] = 0
		elif v[10] < v[12]:
			v[10] = 0
			v[12] = 1
	return dictio
