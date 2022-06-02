from maxheap import MaxHeap

def heapsort(lst):
    sort = []
    max_heap = MaxHeap()
    for idx in lst:
        max_heap.add(idx)
    while max_heap.count > 0:
        max_value = max_heap.retrieve_max()
        sort.insert(0, max_value)
    return sort