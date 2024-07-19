class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if (n + self.size > self.capacity) or (n < 0):
            raise ValueError("Invalid number of cookies")
        self.size += n

    def withdraw(self, n):
        if n > self.size or n < 0:
            raise ValueError("Invalid number of cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
        