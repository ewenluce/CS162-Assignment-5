# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        self._heap.append(node)

        index = self._heap.length() - 1

        while index > 0:
            parent = (index - 1) // 2

            if self._heap.get_at_index(index) < self._heap.get_at_index(parent):
                current_val = self._heap.get_at_index(index)
                parent_val = self._heap.get_at_index(parent)
                self._heap.set_at_index(index, parent_val)
                self._heap.set_at_index(parent, current_val)
                index = parent
            else:
                break

    def is_empty(self) -> bool:
        return self._heap.is_empty()

    def get_min(self) -> object:
        if self._heap.is_empty():
            raise MinHeapException

        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        if self._heap.is_empty():
            raise MinHeapException

        min_val = self._heap.get_at_index(0)
        last_index = self._heap.length() - 1

        if last_index == 0:
            self._heap.remove_at_index(0)
        else:
            last_val = self._heap.get_at_index(last_index)
            self._heap.set_at_index(0, last_val)
            # removing the LAST index is O(1) for DynamicArray
            self._heap.remove_at_index(last_index)
            _percolate_down(self._heap, 0)

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        new_heap = DynamicArray()

        for i in range(da.length()):
            new_heap.append(da.get_at_index(i))

        self._heap = new_heap

        n = self._heap.length()
        for parent in range(n // 2 - 1, -1, -1):
            _percolate_down(self._heap, parent)

    def size(self) -> int:
        return self._heap.length()

    def clear(self) -> None:
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    n = da.length()

    for parent in range(n // 2 - 1, -1, -1):
        _percolate_down(da, parent, n)

    end = n - 1
    while end > 0:
        first_val = da.get_at_index(0)
        end_val = da.get_at_index(end)
        da.set_at_index(0, end_val)
        da.set_at_index(end, first_val)

        _percolate_down(da, 0, end)
        end -= 1

    left = 0
    right = n - 1
    while left < right:
        left_val = da.get_at_index(left)
        right_val = da.get_at_index(right)
        da.set_at_index(left, right_val)
        da.set_at_index(right, left_val)
        left += 1
        right -= 1


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    if size is None:
        size = da.length()

    while True:
        left = 2 * parent + 1
        right = 2 * parent + 2
        smallest = parent

        if left < size and da.get_at_index(left) < da.get_at_index(smallest):
            smallest = left

        if right < size and da.get_at_index(right) < da.get_at_index(smallest):
            smallest = right

        if smallest == parent:
            break

        parent_val = da.get_at_index(parent)
        smallest_val = da.get_at_index(smallest)
        da.set_at_index(parent, smallest_val)
        da.set_at_index(smallest, parent_val)

        parent = smallest


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference the same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
