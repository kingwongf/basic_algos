def non_recur_fib(n, d=[1,1]):
    while len(d) <n:
        d.append(d[-1] + d[-2])
    return d

print(len(non_recur_fib(100)))