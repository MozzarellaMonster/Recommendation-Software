#Codecademy's implementation of the heapsort algorithm
from maxheap import MaxHeap

def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for movie_tuple in lst:
        max_heap.add(movie_tuple)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
    return sort