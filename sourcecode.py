import math
import random

def Find_Kth_Smallest(arr, k):

    if not arr or not (1 <= k <= len(arr)):
        raise ValueError("Invalid array or k out of bounds")
    
    if len(arr) == 1:
        return arr[0]

    pivot = arr[math.floor(random.random() * len(arr))]
    smaller = []
    equal = []
    larger = []

    for x in arr:
        if x > pivot:
            larger.append(x)
        elif x == pivot:
            equal.append(x)
        elif x < pivot:
            smaller.append(x)

    if k <= len(smaller):
        return Find_Kth_Smallest(smaller, k)
    elif k <= len(smaller) + len(equal):
        return pivot
    else:
        return Find_Kth_Smallest(larger, k - len(smaller) - len(equal))


def main():
    print(Find_Kth_Smallest([5, 1, 6, 7, 3, 4, 8], 3))   # should print 4

if __name__ == "__main__":
    main()