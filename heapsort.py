# Codecademy's implementation of the heapsort algorithm
# altered to better fit program's purpose
from maxheap import MaxHeap

def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for movie_tuple in lst:
        max_heap.add(movie_tuple)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.append(max_value)
    return sort