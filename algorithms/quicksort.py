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

def qsort1(array, left, right):  
    def swap(array, s, d):  
        if s != d:  
            tmp = array[s]  
            array[s] = arr[d]  
            array[d] = tmp  
    if l >= r:  
        return      
    m = l  
    for i in range(left, right):  
        if array[i] <= array[right]:  
            swap(arr, i, m)  
            m += 1  
    swap(array, m, right)  
    qsort3(array, left, m-1)  
    qsort3(array, m+1, right)  
    return array 
