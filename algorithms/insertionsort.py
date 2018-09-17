import numpy as np

def instance(size, order):
	# TODO: Improve randomness of the data variance
	if order == 'ASC':
		array = list(range(0, size))
		return array

	if order == 'DESC':
		array = list(range(0, size))
		array = list(reversed(array))
		return array

	if order == 'RAND':
		array = list(range(0, size))
		array = np.random.shuffle(array)
		return array
	return []

def insertionSort(array, size):
	for i in range(1, size):
		if array[i] >= array[i - 1]:
			continue
		for j in range(i):
			if array[i] < array[j]:
				array[j], array[j + 1:i + 1] = array[i], array[j:i]
				break
	return array

array = instance(100000, 'DESC')
print(array)
array = insertionSort(array, 100000)
print (array)
