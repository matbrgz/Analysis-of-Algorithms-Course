def shell_sort(array, size):
	inc = size // 2
	while inc:
		for i, el in enumerate(array):
			while i >= inc and array[i - inc] > el:
				array[i] = array[i - inc]
				i -= inc
			array[i] = el
		inc = 1 if inc == 2 else int(inc * 5.0 / 11)
	return array
