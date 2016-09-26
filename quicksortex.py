# Quicksort
# Time complexity:
# worst case: o(n^2)
# average case: o(n*log(n))
# best case: o(n*log(n))
def quicksortex(x):
    quicksorth(x,0,x.size-1)
    return x

def quicksorth(A,lo,hi):
    if lo < hi :
        p = partition(A,lo,hi)
        quicksorth(A,lo,p)
        quicksorth(A,p+1,hi)

def partition(A,lo,hi):
    pivot = A[lo]
    i = lo+1
    j = hi
    while True:
        while i <= j and A[i] < pivot :
            i = i + 1
        while j >= i and A[j] >= pivot :
            j = j - 1
        if j < i :
            A[j],A[lo] = A[lo],A[j]
            return j
        A[i],A[j] = A[j],A[i]
