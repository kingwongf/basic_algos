def sth_f(a, b=[]):
    b.append(a)
    return b

def sth_g(a):
    b = []
    b.append(a)
    return b
print(sth_f(5))
print(sth_f(6))

print(sth_g(5))
print(sth_g(6))