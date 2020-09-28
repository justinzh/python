# Metaclass that adds tracing decordator to every mehtod of a client class

from types import FunctionType
from decotools import tracer

def decorateAllm(decorator):
    class MetaTrace(type):
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    print(attr, attrval)
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaTrace

class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:
                print(attr, attrval)
                classdict[attr] = tracer(attrval)
        return type.__new__(meta, classname, supers, classdict)

def decorateAll(decorator):
    def decoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) == FunctionType:
                setattr(aClass, attr, decorator(attrval))
        return aClass
    return decoDecorate

if __name__ == '__main__':
    # class Person(metaclass = MetaTrace):
    # class Person(metaclass = decorateAll(tracer)):
    @decorateAll(tracer)
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)

        def lastName(self):
            return self.name.split()[-1]

    bob = Person('bob Smith', 50000)
    sue = Person('Sue jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)
    print('%.2f' % sue.pay)
    print(bob.lastName(), sue.lastName())