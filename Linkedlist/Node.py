class Node:
    
    def __init__(self, element):
        self.element = element
        self.next = None

    def __str__(self):
        return f"{self.element}:{self.next is not None}"