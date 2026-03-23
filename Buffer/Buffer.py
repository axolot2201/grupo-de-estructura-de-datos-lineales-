class CircularBuffer:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self):
        self.capacity = 5
        self.elements = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    
    # return an str of the collection
    def __str__(self):
        result = []
        i = self.head
        for _ in range(self.size):
            result.append(self.elements[i])
            i = (i + 1) % self.capacity
        return str(result)
    
    # return the length of the elements in the collection
    def __len__(self):
        return self.size

    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return self.size == 0
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        i = self.head
        count = 0
        while count < self.size:
            yield self.elements[i]
            i = (i + 1) % self.capacity
            count += 1
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        for item in self:
            if item == element:
                return True
        return False
    
    # add the element to the end of the collection
    # ERROR: if the collection is full before adding a new element
    def push(self, element):
        if self.size == self.capacity:
            raise Exception
    
        self.elements[self.tail] = element
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
    
    # remove and return the next element in the collectio
    # ERROR: if the collection is empty 
    def pop(self, index):
        if self.isEmpty():
            raise Exception("Buffer is empty")
        
        element = self.elements[self.head]
        self.elements[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return element
    
    # remove all elements in the collection
    def clear(self):
        self.elements = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0