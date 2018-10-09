def selection_sort(array, size):
	if size < 2:
		return array
	else:
		for i in range(size):
				mini = min(array[i:])  # find minimum element
				min_index = array[i:].index(mini)  # find index of minimum element
				array[i + min_index] = array[i]  # replace element at min_index with first element
				array[i] = mini  # replace first element with min element
		return array
