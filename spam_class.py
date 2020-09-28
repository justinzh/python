#! spam_class.py

class Spam:
        numInstances = 0
        def __init__(self): 
            self.counter()
        
        @classmethod
        def printNumInstances(cls):
            print('The total instances for %s is %s' % (cls.__name__, cls.numInstances))
        @classmethod
        def counter(cls):
            cls.numInstances += 1

class Sub(Spam):
    def printNumInstances(cls): 
        print('...')
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class SubWithDM(Spam):
    numInstances = 0
    def printNumInstances(cls):
        print('xxxx')
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class SubWithD(Spam):
    numInstances = 0


        