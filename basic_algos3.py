
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
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



def recur_fib(n):
    if n ==1:
        return 1
    elif n==2:
        return 1
    else:
        return recur_fib(n-1) + recur_fib(n-2)

def prime_sieve(n):
    primes = [True]*(n+1)
    p=2
    while p*p<=n:
        if primes[p]:
            for j in range(p*2,n+1,p):
                primes[j] = False
        p+=1

    return [p for p in range(n+1) if primes[p]]

def non_recur_fib(n):
    d=[1,1]
    while len(d)< n:
        d.append(d[-1]+d[-2])
    return d
def merge_sort2(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort2(L)
        merge_sort2(R)
        i=j=k=0
        while len(L) > i and len(R) > j:
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while len(L) >i:
            arr[k] = L[i]
            i+=1
            k+=1
        while len(R) >j:
            arr[k] = R[j]
            j+=1
            k+=1
        return arr

def binary_search(arr, elem):
    print(list(zip(arr, list(range(len(arr))))))
    sorted_arr = merge_sort(arr)
    lb = 0
    ub = len(sorted_arr) -1
    while lb <=ub:
        mid = (lb +ub)//2
        if sorted_arr[mid] > elem:
            ub = mid -1
        elif sorted_arr[mid] < elem:
            lb = mid +1
        elif sorted_arr[mid] == elem:
            return mid
    return 'not in list'

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if swapped is False:
            return arr

def part(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = part(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def beta(X,y):
    import numpy as np
    return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

def nonrecur_factorial(n):
    r=n
    for i in range(1,n-1):
        r*=(n-i)
    return r

def combinations(n,k):
    '''
    nCr = n!/((n-k)!*(k!))
        = (n*(n-1)*(n-2) *...*(n-k+1))/ (k(k-1)(k-2)*...*(1))
    :param n:
    :param k:
    :return:
    '''

    r = 1
    for i in range(k):
        r*= (n-i)
        r= r/(i+1)
    return r

def permutation(n,k):
    '''
    nPr = n!/k!
        = n(n-1)(n-2)*...*(n-k+1)
    :param n:
    :param k:
    :return:
    '''
    r = 1
    for i in range(k):
        r*= (n-i)
    return r



def part2(arr, low, high):
    i = low-1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i +1
def quicksort2(arr,low,high):
    if low < high:
        pi = part2(arr,low,high)
        quicksort2(arr, low, pi-1)
        quicksort2(arr, pi+1, high)


print('merge sort')
print(merge_sort([6,4,2,1,7,4,3]))
print("non recur fib")
print(non_recur_fib(10))
print("recur fib")
print(recur_fib(10))

print('merge sort 2')
print(merge_sort([6,4,2,1,7,4,3]))
print('bubble sort')
print(merge_sort([6,4,2,1,7,4,3]))

print('binary search')
print(binary_search([6,4,2,1,7,4,3], 3))
print([6,4,2,1,7,4,3].index(3))

print('quick sort')
li = [6,4,2,1,7,4,3]
low = 0
high = len(li)-1
quick_sort(li, low,high)
print(li)
