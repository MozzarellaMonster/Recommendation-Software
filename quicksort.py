#File containing the quicksort algorithm I'll be using.
from random import randrange

def quicksort(unsorted_list, start, end):
    if start >= end:
        return

    pivot_index = randrange(start, end + 1)
    pivot_element = unsorted_list[pivot_index]

    unsorted_list[end], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[end]

    less_than_pointer = start

    for i in range(start, end):
        if unsorted_list[i] < pivot_element:
            unsorted_list[i], unsorted_list[less_than_pointer] = unsorted_list[less_than_pointer], unsorted_list[i]