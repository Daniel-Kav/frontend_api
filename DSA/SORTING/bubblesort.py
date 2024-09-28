
# def bubble_sort(arr):
#     # get the length of the arr?
#     n = len(arr)

#     # iterate through the array elementa
#     for i in range(n):
#         # track if there is a swap in the iteration
#         swapped = False
#         # loop minus the last element which is already sorted
#         for j in range(0, n-i-1):
#             # swap the element if it is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         # if there was no swap in the last pass then break 
#         if not swapped:
#             break

def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j],arr[j + 1] = arr[j+1],arr[j]
                swapped = True
                swaps += 1
        if not swapped:
            break
    return swaps
        
# Example usage
# arr = [64, 34, 25, 12, 22,30, 11, 90,300,20,457,390,300,497,1284]
arr = [(2, 3), (1, 2), (4, 1)]
print(bubble_sort(arr))
print("Sorted array is:", arr)