import time

def binary_search(array,x):
    LB = 0
    UB = len(array)-1
    while LB<=UB:
        mid = (UB+LB)//2
        if array[mid] > x:
            UB = mid - 1
        elif array[mid] < x:
            LB = mid + 1
        elif array[mid] == x:
            return mid

    return 'does not exist!'

def merge_sort(array):
    if len(array) > 1:

        mid = (len(array))//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)

        i=j=k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            array[k] = L[i]
            i+=1
            k+=1
        while j <len(R):
            array[k] = R[j]
            j+=1
            k+=1
        return array

def bubble_sort(arr):
    for i in range(len(arr)):
        swapped=False
        for j in range(len(arr)-1-i): ## Remember len(arr)-1-i !!!!!
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if swapped is False:
            return arr

def binomia_coeff(n,k):
    res = 1
    for i in range(n):
        res*=i
        res/=()


print(merge_sort([9,8,7,6,4,3,3,1]))
print(bubble_sort([9,8,7,6,4,3,3,1]))

print(binary_search([1,2,3,4,7,8,9],4))