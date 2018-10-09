# To add an item to the top of the stack, use append()
class stack(list):
	''' push() to add an item to the top of the stack '''
	push = list.append


# non-recursive quicksort
def quick_sort(array, size):
	"""
	Sort a sequence using the quick-sort algorithm.

	:param array: the sequence to be sorted
	:return: array, sorted
	"""
	if size < 2:
		return array
	todo = stack([(0, size - 1)])
	while todo:
		elem_idx, pivot_idx = low, high = todo.pop()
		elem = array[elem_idx]
		pivot = array[pivot_idx]
		while pivot_idx > elem_idx:
			if elem > pivot:
				array[pivot_idx] = elem
				pivot_idx -= 1
				array[elem_idx] = elem = array[pivot_idx]
			else:
				elem_idx += 1
				elem = array[elem_idx]
		array[pivot_idx] = pivot

		lsize = pivot_idx - low
		hsize = high - pivot_idx
		if lsize <= hsize:
			if 1 < lsize:
				todo.push((pivot_idx + 1, high))
				todo.push((low, pivot_idx - 1))
		else:
			todo.push((low, pivot_idx - 1))
		if 1 < hsize:
			todo.push((pivot_idx + 1, high))
	return array