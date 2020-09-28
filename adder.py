#! test work 
"""
drill test class for class inheritances
"""

from classtools import AttrDisplay
class Adder:
    def __init__(self, value):
        self.data = value
    def add(self, x, y):
        print('Not implemented')
    def __add__(self, y):
        self.data = self.add(self.data, y)
        return self

class ListAdder(AttrDisplay, Adder):
    def add(self, x, y):
        return list(x) + list(y)

class DictAdder(AttrDisplay, Adder):
    def add(self, x, y):
        return dict(x, **y)

class MyList():
    """
    MyList 
    """
    def __init__(self, value=[]):
        print('value:%s' % value)
        self.data = value[:]

    def __add__(self, x):
        return MyList(self.data + x)
    
    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)
        
    def __repr__(self):
        return repr(self.data)

    def __getattr__(self, name):
        print('__getattr__')
        return getattr(self.data, name)


class MyListSub(MyList):
    counter = 0
    def __init__(self, data = []):
        MyList.__init__(self, data)
        self.counter += 1

    def __add__(self, y):
        self.counter += 1
        print(' + call counter: %s' % self.counter)
        return MyListSub(MyList.__add__(self, y))

    def printcounter(self):
        print('operator + overloading method was called %s times' % self.counter)

class Attrs:
    #def __init__(self):
    #    self.bar = 'hello'

    def __getattribute__(self, x):
        print('Fetching attribut: %s' % x)

    def __setattr__(self, name, value):
        print('Setting attribute: %s = %s' % (name, value))

class MySet():
    def __init__(self, data):
        self.data = data
    
    def __and__(self, x):
        return MySet(list(i for i in self.data if i in x))

    def __or__(self, x):
        return MySet(self.data + list(i for i in x if i not in self.data))

    def __repr__(self):
        return '[%s]' % ','.join(map(str,self.data))
    
    def __getitem__(self, ind):
        if ':' in str(ind):
            return MySet(self.data[ind])
        return self.data[ind]

class MySetSub(MySet):
    def intersect(self, *args):
        res = []
        for x in self.data:
            for lp in args:
                if x not in lp:
                    break
            else:
                res.append(x)
        return MySetSub(res)
    
    def union(*args):
        res = []
        for lp in args:
            for item in lp:
                if item not in res:
                    res.append(item)
        return MySetSub(res)