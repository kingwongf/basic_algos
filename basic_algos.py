import numpy as np

def binary_search(array, x):
    found = False
    LB, UB = 0, len(array)
    while found is False:
        mid = (UB+LB)//2
        if array[mid] <x:
            LB = mid +1
        elif array[mid] >x:
            UB = mid -1
        elif array[mid]==x:
            found = True
            return mid

def bubble_sort(array):
    for i in range(len(array)):
        swapped=False
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped =True
        if swapped is False:
            return array

def merge_sort(array):
    if len(array)>1:
        mid= len(array)//2
        L=array[:mid]
        R=array[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k=0
        while i <len(L) and j<len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
        while i <len(L):
            array[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            array[k] = R[j]
            j+=1
            k+=1
        return array

def fibonacci(n):
    if n<=0:
        print("incorrect")
    elif n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def prime_sieve(n):
    prime = [True for n in range(n+1)]
    p=2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p+=1
    prime[0] = False
    prime[1] = False
    return [p for p in range(n+1) if prime[p]]

print(bubble_sort([9,8,7,6,4,3,3,1]))
print(binary_search([0,1,2,3.3,3.4,4,5.55,6.77,7,8,9], 5.55))
print(bubble_sort([1,2,9,8,6,4,5,3,9,8]))
print(merge_sort([1,2,9,8,6,4,5,3,9,8]))
print([fibonacci(n) for n in range(1,10)])
print(prime_sieve(20))