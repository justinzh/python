# implement iterator/iterable with class and operator overload

class SquareArray:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter >= self.limit:   
            raise StopIteration
        self.counter += 1
        return self.counter**2
    
class SquareArrayIterable:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        return SquareArrayIter(self.limit)

class SquareArrayIter:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        self.counter += 1
        return self.counter**2

class NSerial:
    def __init__(self, value):
        self.value = value
    def npower(self, i):
        if i == 0:
            return 1
        else:
            return i*self.npower(i-1)
    def __iter__(self):
        for i in range(self.value):
            yield self.npower(i)
    def __getitem__(self, ind):
        return self.npower(ind)
        

    