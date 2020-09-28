# file timerdeco1.py
# Caveat: timer won't work on method as coded

import time, sys
force = list if sys.version_info[0] == 3 else (lambda X: X)

def timer(label = '===>', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):
            start = time.perf_counter()
            result = self.func(*args, **kargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                print('%s %s: %.10f, %.10f' % (label, self.func.__name__, elapsed, self.alltime))
            return result
    return Timer

@timer('xxxx', True)
def listcomp(N):
    return [x*2 for x in range(N)]

@timer('yyyy', True)
def mapcall(N):
    return force(map((lambda x: x*2), range(N)))

result = listcomp(5)
listcomp(50000)
listcomp(500000)
listcomp(100000)
print(result)
print('allTime = %s' % listcomp.alltime)

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime =%s' % mapcall.alltime)

print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))


