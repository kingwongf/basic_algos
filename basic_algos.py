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

def partition(arr, low, high):
    i = low -1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <=pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi -1)
        quicksort(arr, pi + 1, high)

def non_recur_fib(n, d=[1,1]):
    while len(d) <n:
        d.append(d[-1] + d[-2])
    return d

def merge_sort_2(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort_2(L)
        merge_sort_2(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
        return arr

def bubble_sort_2(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if swapped==False:
            return arr

def prime_sieve(n):
    prime= [True for n in range(n+1)]
    p=2
    while p*p <= n:
        if prime[p]:
            for i in range(p*2, n+1,p):
                prime[i] = False
        p+=1
    return [p for p in range(n+1) if prime[p]]

def screwy_pirate(n):
    return 2*n-1

print("prime sieve")
print(prime_sieve(20))


print("screwy pirates ")
for i in range(10):
    print(screwy_pirate(i))

print("fib umber")
print(non_recur_fib(10))

print("quick sort")
li = [5,2,7,1,9]
n= len(li)-1
quicksort(li, 0, n)
print(li)

print("merge sort 1")
print(merge_sort([7,3,5,2,8]))
print("merge sort 2")
print(merge_sort_2([7,3,5,2,8]))

print("bubble sort")
print(bubble_sort_2([7,3,5,2,8]))



print(bubble_sort([9,8,7,6,4,3,3,1]))
print(binary_search([0,1,2,3.3,3.4,4,5.55,6.77,7,8,9], 5.55))
print(bubble_sort([1,2,9,8,6,4,5,3,9,8]))
print(merge_sort([1,2,9,8,6,4,5,3,9,8]))
print([fibonacci(n) for n in range(1,10)])
print(prime_sieve(20))