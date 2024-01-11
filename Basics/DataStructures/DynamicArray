# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.

class DynamicArray:
    
# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
    def __init__(self, capacity: int):
        self.list = [None] * capacity
        self.capacity = capacity
        self.index = 0
        return

# int get(int i) will return the element at index i. Assume that index i is valid.
    def get(self, i: int) -> int:
        # Assune i index is valid
        return self.list[i]

# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    def set(self, i: int, n: int) -> None:
        self.list[i] = n

# void pushback(int n) will push the element n to the end of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.
    def pushback(self, n: int) -> None:
        if self.index == self.capacity:
            self.resize()

        self.list[self.index] = n
        self.index += 1

        '''
        for i in self.list:
            if i == None:
                self.list[i] = n
                self.index = i
                return
            
        # otherwise there was no empty place to put the element
        self.resize()
        newHalfIndex = self.capacity / 2
        self.list[newHalfIndex] = n
        '''

# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    def popback(self) -> int:
        if self.index > 0:
            self.index -= 1

        return self.list[self.index]

        '''
        for i in range(self.capacity, 0, -1):
            if self.list[i] != None:
                elem = self.list[i]
                self.list[i] = None
                self.index = i

                return elem
        return 0
        '''

# void resize() will double the capacity of the array.
    def resize(self) -> None:
        sizeAddition = [None] * self.capacity

        self.list = self.list + sizeAddition
        self.capacity *= 2

        return

# int getSize() will return the number of elements in the array.
    def getSize(self) -> int:
        return self.index
    
# int getCapacity() will return the capacity of the array.
    def getCapacity(self) -> int:
        return self.capacity