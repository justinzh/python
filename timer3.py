# File timer3.py (2.X and 3.X)
"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4)
_reps times, and returns total time for all runs, with final result.
bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attempt to
filter out system load variation, and returns best time among _reps tests.
bestoftotal(spam 1, 2, a=3, b=4, _rep1=5, reps=1000) runs best-of-totals
test, which takes the best among _reps1 runs of (the total of _reps runs);
"""
import time, sys

timer = time.perf_counter

def total(func, *pargs, _reps = 1000, **kargs):
    replist = list(range(_reps))
    start = timer()
    for i in replist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

# Passed-in or default reps
# Host range out for 2.X lists
def bestof(func, *pargs, _reps = 5, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, _reps1 = 5, **kargs):
    return min(total(func, *pargs, **kargs) for i in range(_reps1))
