#Codecademy's implementation of the MaxHeap data structure
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
        print("Adding: {0} to {1}".format(movie_tuple, self.heap_list))
        self.heap_list.append(movie_tuple)
        self.heapify_up()
    
    def heapify_up(self):
        print("Heapifying up")
        index = self.count
        while self.parent_idx(index) > 0:
            child = self.heap_list[index]
            parent = self.heap_list[self.parent_idx(index)]
            if parent[1] < child[1]:
                print("swapping {0} with {1}".format(parent, child))
                self.heap_list[index] = parent
                self.heap_list[self.parent_idx(index)] = child
            index = self.parent_idx(index)
        parent("Heap restored {0}".format(self.heap_list))

    def retrieve_max(self):
        if self.count == 0:
            print("No items in heap")
            return None
        max_value = self.heap_list[1]
        print("Removing: {0} from {1}".format(max_value, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        self.heapify_down()
        return max_value
    
    def heapify_down(self):
        index = 1
        while self.child_present(index):
            print("Heapifying down!")
            larger_child_index = self.get_larger_child_idx(index)
            child = self.heap_list[larger_child_index]
            parent = self.heap_list[index]
            if parent < child:
                self.heap_list[index] = child
                self.heap_list[larger_child_index] = parent
            index = larger_child_index
        print("HEAP RESTORED! {0}".format(self.heap_list))
    
    def get_larger_child_idx(self, index):
        if self.right_child_idx(index) > self.count:
            print("There is only a left child")
            return self.left_child_idx(index)
        else:
            left_child = self.heap_list[self.left_child_idx(index)]
            right_child = self.heap_list[self.right_child_idx(index)]

            if left_child[1] > right_child[1]:
                print("Left child " + str(left_child) + " is larger than right child " + str(right_child))
                return self.left_child_idx(index)
            else:
                print("Right child " + str(right_child) + " is larger than left child " + str(left_child))
                return self.right_child_idx(index)