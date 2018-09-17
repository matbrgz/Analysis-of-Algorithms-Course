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

def heapsort(array):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((size-2)/2, -1, -1):
    siftdown(array, start, size-1)
 
  for end in range(len(lst)-1, 0, -1):
    array[end], array[0] = array[0], array[end]
    siftdown(array, 0, end - 1)
  return array
 
def siftdown(array, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and array[child] < array[child + 1]:
      child += 1
    if array[root] < array[child]:
      array[root], array[child] = array[child], array[root]
      root = child
    else:
      break
