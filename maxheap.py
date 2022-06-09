# Codecademy's implementation of the MaxHeap data structure
# altered to better fit program's purpose
class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0
    
    def parent_idx(self, index):
        return index//2
    
    def left_child_idx(self, index):
        return index * 2
    
    def right_child_idx(self, index):
        return index * 2 + 1
    
    def child_present(self, index):
        return self.left_child_idx(index) <= self.count
    
    def add(self, movie_tuple):
        self.count += 1
        self.heap_list.append(movie_tuple)
        self.heapify_up()
    
    def heapify_up(self):
        index = self.count
        while self.parent_idx(index) > 0:
            child = self.heap_list[index]
            parent = self.heap_list[self.parent_idx(index)]
            if parent[1] < child[1]:
                self.heap_list[index] = parent
                self.heap_list[self.parent_idx(index)] = child
            index = self.parent_idx(index)

    def retrieve_max(self):
        if self.count == 0:
            return None
        max_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return max_value
    
    def heapify_down(self):
        index = 1
        while self.child_present(index):
            larger_child_index = self.get_larger_child_idx(index)
            child = self.heap_list[larger_child_index]
            parent = self.heap_list[index]
            if parent[1] < child[1]:
                self.heap_list[index] = child
                self.heap_list[larger_child_index] = parent
            index = larger_child_index
    
    def get_larger_child_idx(self, index):
        if self.right_child_idx(index) > self.count:
            return self.left_child_idx(index)
        else:
            left_child = self.heap_list[self.left_child_idx(index)]
            right_child = self.heap_list[self.right_child_idx(index)]

            if left_child[1] > right_child[1]:
                return self.left_child_idx(index)
            else:
                return self.right_child_idx(index)