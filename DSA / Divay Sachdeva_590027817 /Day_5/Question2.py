# Given two arrays, determine whether they are equal. Two arrays are considered equal if they have the same size and corresponding elements are identical..

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

if sorted(arr1) == sorted(arr2):
    print(True)
else:
    print(False)
