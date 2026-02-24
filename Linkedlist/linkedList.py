
# class LinkedList:
    
    # initial_elements: allow the collection to start with some elements
def __init__(self, initial_elements=[]):
        self.head = None
        self.tail = None
        self.size = 0
        
        for element in initial_elements:
            self.append(element)
    
    # return an str of the collection
def __str__(self):
        elements = []
        node = self.head
        
        while node is not None:
            elements.append(node.element)
            node = node.next
            
        return str(elements)
    
    # return the length of the elements in the collection
def __len__(self):
        return self.size
    
    # return the element of the collection in the index possition
    # Error: the index dont exist
def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index dont exist")
        
        node = self.head
        for _ in range(index):
            node = node.next
            
        return node.element
    
    # return a boolean that implies if the collection is empty or not
def isEmpty(self):
        return self.size == 0
    
    # allow the collection to be called in a for loop
def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node.element
            node = node.next
    
    # return a boolean value representing the existence of an element in the collection
def __contains__(self, element):
        node = self.head
        
        while node is not None:
            if node.element == element:
                return True
            node = node.next
                
        return False
    
    # add the element to the end of the collection
def append(self, element):
        new_node = Node(element)
        
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.size += 1
    
    # add the element to the collection at the requested index
    # Error: non existing index in the collection
def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index dont exist")
        
        new_node = Node(element)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            
            if self.size == 0:
                self.tail = new_node
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            
            new_node.next = node.next
            node.next = new_node
            
            if new_node.next is None:
                self.tail = new_node
        
        self.size += 1
    
    # remove an element in the collection by its value
    # Error: the element dont exist in the collection
def remove(self, element):
        node = self.head
        prev = None
        
        while node is not None:
            if node.element == element:
                
                if prev is None:
                    self.head = node.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = node.next
                    if node.next is None:
                        self.tail = prev
                
                self.size -= 1
                return
            
            prev = node
            node = node.next
        
        raise ValueError("Element dont exist")
    
    # remove and return the element in the collection by its index
def pop(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index dont exist")
        
        node = self.head
        prev = None
        
        for _ in range(index):
            prev = node
            node = node.next
        
        if prev is None:
            self.head = node.next
            if self.head is None:
                self.tail = None
        else:
            prev.next = node.next
            if node.next is None:
                self.tail = prev
        
        self.size -= 1
        return node.element
    
    # remove all elements in the collection
def clear(self):
        self.head = None
        self.tail = None
        self.size = 0