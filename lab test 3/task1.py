def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Pivot selection: AI often suggests using the middle element, first, or last element.
        # Here, we use the middle element for better average case performance.
        pivot_index = len(arr) // 2
        pivot = arr[pivot_index]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)

arr = [90, 12, 77, 23, 5, 41, 68]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# AI's suggestion for pivot selection:
# The choice of pivot greatly affects Quick Sort's performance. The pivot can be the first element, 
# last element, a random element, or the middle element (as used above). Random or middle element 
# selection helps avoid the worst-case time complexity on already sorted or nearly sorted data, 
# leading to better average performance. Using the middle element is a simple heuristic 
# that generally yields good performance for random data.
