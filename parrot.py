
class base:
    def line(self):
        print('I am a base.')

class Customer(base):
    def line(self):
        print('I am a customer.')

class Clerk(base):
    def line(self):
        print('I am a clerk.')

class Parrot(base):
    def line(self):
        print('I am a parrot.')


class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()
    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()

if __name__ == '__main__':
    Scene().action()