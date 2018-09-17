import numpy as np
import time

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

def shellSort(array, size):
	start_time = time.time()
	"""Merge sort merging function."""

	# Start with a big gap, then reduce the gap
	gap = size / 2

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped 
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:
		for i in range(gap, size):

			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = array[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and array[j - gap] > temp:
				array[j] = array[j - gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			array[j] = temp
		gap /= 2
	print("--- %s seconds ---" % (time.time() - start_time))
	return array

unsorted = instance(10, 'RAND')
print(unsorted)
sorted = shellSort(unsorted, 10)
print (sorted)
