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

def selectionSort(array, size):
	"""Merge sort merging function."""

	for i in range(size):
		mini = min(array[i:])  # find minimum element
		min_index = array[i:].index(mini)  # find index of minimum element
		array[i + min_index] = array[i]  # replace element at min_index with first element
		array[i] = mini  # replace first element with min element
	return array

array = instance(1000000, 'RAND')
print(array)
array = selectionSort(array, 1000000)
print (array)
