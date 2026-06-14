# Write an efficient function to calculate the sum of all elements in an integer array.

def arraySum(arr):
    total = 0
    for num in arr:
        total += num
    return total

arr = list(map(int, input().split()))
print(arraySum(arr))
