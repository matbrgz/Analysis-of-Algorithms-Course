def insertion_sort(array, size):
	if size < 2:
		return array
	else:
		for i in range(1, size):
			if array[i] >= array[i - 1]:
				continue
			for j in range(i):
				if array[i] < array[j]:
					array[j], array[j + 1:i + 1] = array[i], array[j:i]
					break
		return array
