class Arraylist:
    # size: initial capacity of the collection
    # initial_elements: allow the collection to start with some elements
    def __init__(self, size=100, initial_elements=[]):
        if len(initial_elements) > size:
            raise ValueError()

        self._capacidad = size
        self._datos = [None] * size
        self._longitud = 0

        for element in initial_elements:
            self._datos[self._longitud] = element
            self._longitud += 1
        
    # return an str of the collection
    def __str__(self):
         return str(self._datos[:self._longitud])

    # return the length of the elements in the collection
    def __len__(self):
        return self._longitud

    # return a boolean that implies if the collection is empty or not    
    def isEmpty(self):
        return self._longitud == 0

    # return the element of the collection in the index possition
    # Error: the index dont exist    
    def __getitem__(self, index):
        if index < 0 or index >= self._longitud:
            raise IndexError("Index does not exist")
        return self._datos[index]

    # allow the collection to be called in a for loop    
    def __iter__(self):
        for i in range(self._longitud):
            yield self._datos[i]

    # return a boolean value representing the existence of an element in the collection
    def __contains__(self, element):
        for i in range(self._longitud):
            if self._datos[i] == element:
                return True
        return False

    # add the element to the end of the collection    
    def append(self, element):
        self._datos[self._longitud] = element
        self._longitud += 1

    # add the element to the collection at the requested index
    # Error: non existing index in the collection
    def insert(self, index, element):
        if index < 0 or index > self._longitud:
            raise IndexError("Non existing index in the collection")
        
        for i in range(self._longitud, index, -1):
            self._datos[i] = self._datos[i - 1]

        self._datos[index] = element
        self._longitud += 1

    # remove an element in the collection by its value
    # Error: the element dont exist in the collection    
    def remove(self, element):
        for i in range(self._longitud):
            if self._datos[i] == element:

                for j in range(i, self._longitud - 1):
                    self._datos[j] = self._datos[j + 1]

                self._datos[self._longitud - 1] = None
                self._longitud -= 1
                return

        raise ValueError("Element does not exist in the collection")

    # remove and return the element in the collection by its index    
    def pop(self, index):
        if index < 0 or index >= self._longitud:
            raise IndexError("Index does not exist")

        value = self._datos[index]

        for i in range(index, self._longitud - 1):
            self._datos[i] = self._datos[i + 1]

        self._datos[self._longitud - 1] = None
        self._longitud -= 1

        return value

    # remove all elements in the collection    
    def clear(self):
        self._datos = [None] * self._capacidad
        self._longitud = 0