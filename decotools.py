# File decotools.py: assorted decorator tools

import time

def tracer(func):
    calls = 0
    def onCall(*args, **kargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kargs)
    return onCall

def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kargs):
            start = time.perf_counter()
            result = func(*args, **kargs)
            elapsed = time.perf_counter - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%: %0.5f, %0.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator



if __name__ == '__main__':
    class Person:
        @tracer
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)

        @tracer
        def lastName(self):
            return self.name.split()[-1]

    bob = Person('bob Smith', 50000)
    sue = Person('Sue jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)
    print('%.2f' % sue.pay)
    print(bob.lastName(), sue.lastName())

