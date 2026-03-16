class Stack:
    
    # initial_elements: allow the collection to start with some elements
    def __init__(self, initial_elements=[]):
        self.elements = list(initial_elements)
    
    # return an str of the collection
    def __str__(self):
        return str(self.elements)
    
    # return the length of the elements in the collection
    def __len__(self):
        return len(self.elements)
    
    # return a boolean that implies if the collection is empty or not
    def isEmpty(self):
        return len(self.elements) == 0
    
    # return the next element in the collection
    def peek(self):
        return self.elements[-1]
    
    # allow the collection to be called in a for loop
    def __iter__(self):
        return iter(self.elements)
    
    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        return element in self.elements
    
    # add the element to the collection
    def push(self, element):
        self.elements.append(element)
    
    # remove and return the next element in the collection
    def pop(self, index):
        return self.elements.pop()