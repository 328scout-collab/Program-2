import random

def Find_Kth_Smallest(arr, k):

    #Validates that the array is not empty and has a valid k
    if not arr or not (1 <= k <= len(arr)):
        raise ValueError("Invalid array or k out of bounds")

    #Base Case
    if len(arr) == 1:
        return arr[0]
    
    #Choose random pivot
    pivot = random.choice(arr)

    #Partition array into smaller lists based on pivot
    #smaller, equal, and larger values
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    #Determine recurse direction
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