#! python
# File testmixin.py

"""
Genric lister mixin tester: similar to transitive reloader in
Chapter 25, but passes a class object to tester (not function),
and testByNames adds loading of both module and class by name
strings here, in keeping with Chapter 31's factories pattern.
"""

import importlib

def tester(listerclass, sept=False):

    class Super:
        data1 = 'SPAM'
        def __init__(self):
            self.data1 = 'spam'
        def ham(self):
            pass

    class Sub(Super, listerclass):
        def __init__(self):
            #Super.__init__(self)
            self.data2 = 'egg'
            self.data3 = 42
        def spam(self):
            pass

    instance  = Sub()
    print(instance)
    if sept: print('-'*80)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listclass = getattr(modobject, classname)
    tester(listclass, sept)

if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True)
    #testByNames('listinherited', 'ListInherited', True)
    #testByNames('listtree', 'ListTree', False)



