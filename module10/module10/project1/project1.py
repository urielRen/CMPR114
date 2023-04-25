# Uriel Renteria
# 4/24/23

class A(B):
    def one(self):
        print('1')

    def two(self):
        print('2')

class B(A):
    def three(self):
        print('3')

    def four(self):
        print('4')

a1 = A()
a1.one()
a1.two()
a1.three()
a1.four()

#b1 = B()
#b1.three()
#b1.four()

#b1.one()
#b1.two()
#b1.three()
#b1.four()