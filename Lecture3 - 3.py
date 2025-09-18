class A:
    pass

class B(A): pass

class C(B ,A): pass

class D(B, C): pass

print(D.mro())

