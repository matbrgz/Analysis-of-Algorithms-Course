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

def merge(left, right):
	"""Merge sort merging function."""

	left_index, right_index = 0, 0
	result = []
	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1

	result += left[left_index:]
	result += right[right_index:]
	return result


def mergeSort(array, size):
	"""Merge sort algorithm implementation."""

	if size <= 1:  # base case
		return array

	# divide array in half and merge sort recursively
	half = size // 2
	left = mergeSort(array[:half], half)
	right = mergeSort(array[half:], half)

	return merge(left, right)

array = instance(1000000, 'RAND')
print(array)
array = mergeSort(array, 1000000)
print (array)
