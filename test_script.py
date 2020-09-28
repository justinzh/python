l = [1,2,4,8,16,32,64]
x= 5
i=0
while i<len(l):
    if 2**x == l[i]:
        print('i found %s' % i)
        break
    i += 1
else:
    print('nothing found')

for a in range(len(l)):
    if 2**x == l[a]:
        print('i found %s' % a)
        break
else:
    print('nothing found')


try:
    print('try')
    x = 1/0
except:
    print('exception caught')
finally:
    print('finally')
print('afterwards')

        