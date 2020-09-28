# File timeseqs.py
"Test the relative speed of iteration tool alternatives."
import sys, timer2

print('starting...')
reps = 10000
repslist = list(range(reps))
# Import timer functions
# Hoist out, list in both 2.X/3.X
def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))

# return map(abs, repslist)
# Use list() here in 3.X only!
def genExpr():
    return list(abs(x) for x in repslist) # list() required to force results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen()) # list() required to force results

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)

# for test in (forLoop, listComp, mapCall, genExpr, genFunc):
#    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
        (test.__name__, total, result[0], result[-1]))

