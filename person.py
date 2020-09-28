# File person.py (start)

# Add record fields initialization

from classtools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    #@rangetest(percent=(0.0, 1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.1) : 
        Person.giveRaise(self, percent+bonus)

if __name__ == '__main__':
#self test code
    bob = Person('Bob Smith')
    sue = Person('Sure Jones', job = 'dev', pay=10000)
    tom = Manager('Tom Jones', 50000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName())
    print(sue.giveRaise(.10))
    print(sue)
    tom.giveRaise(.10)
    print(tom)

    print('all three...')
    for guy in (bob, sue, tom):
        guy.giveRaise(0.1)
        print(guy)
