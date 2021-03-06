
class A:
    def __init__(self):
        """
        Init class A.
        """
        print 'Class A.'

    def fun(self):
        print "A's fun."


class B:
    def __init__(self):
        """
        Init class B.
        """
        print 'Class B.'
        self.member_b = 'B member.'

    def _fun(self):
        print "B's fun."
        self.fun()


class C(A, B):
    def __init__(self):
        """
        Init class C.
        """
        A.__init__(self)
        B.__init__(self)
        print 'Class C'
        self.member_c = 'C member.'

class D(B):
    def __init__(self):
        """
        Init class D.
        """
        print 'Class D.'

    def fun(self):

        print "D's fun."

if __name__ == "__main__":
    c = C()
    ret = c._fun()
    print ret
