from heapq import heappush,heappop

def heap_sort(array, size):
	h = []
	for value in array:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]