def merge(left, right):
	"""Merge sort merging function."""
	merged_array=[]
	while left or right:
		if not left:
			merged_array.append(right.pop())
		elif (not right) or left[-1] > right[-1]:
			merged_array.append(left.pop())
		else:
			merged_array.append(right.pop())
	merged_array.reverse()
	return merged_array

def merge_sort(array, size):
	"""Merge sort algorithm implementation."""
	if size < 2:  # base case
		return array
	else:
		# divide array in half and merge sort recursively
		half = size // 2
		left = merge_sort(array[:half], half)
		right = merge_sort(array[half:], half)
		return merge(left, right)
