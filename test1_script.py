class Exitloop(Exception): pass

i = 9
try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop
                print('loop3" %s' %i)
            print('loop2')
        print('loop1')
except Exitloop:
    print('contiue...')

print(i)

import sys

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raise0():
    raise General

def raise1():
    raise Specific1

def raise2():
    raise Specific2


for func in (raise0, raise1, raise2):
    try:
        func()
    except Specific1:
        print('exception caught:%s' % sys.exc_info()[0])
        print(sys.exc_info())
    except Specific2:
        print('exception caught:%s' % sys.exc_info()[0])
        print(sys.exc_info())
    except General:
        print('exception caught:%s' % sys.exc_info()[0])
        print(sys.exc_info())



