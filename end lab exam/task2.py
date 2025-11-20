"""
Warehouse Inventory Search Module

This module provides two searching strategies for warehouse items:
    - Linear Search: for unsorted/general lists
    - Binary Search: for sorted lists

Functions:
    linear_search(items, target): Search for target using linear scan.
    binary_search(items, target): Search for target using binary search (requires sorted input).

Includes example test cases.
"""

def linear_search(items, target):
    """
    Perform a linear search for `target` in `items`.

    Args:
        items (list): List of warehouse items (any comparable type).
        target: The item to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    for idx, item in enumerate(items):
        if item == target:
            return idx
    return -1

def binary_search(items, target):
    """
    Perform a binary search for `target` in a sorted list `items`.

    Args:
        items (list): Sorted list of warehouse items (any comparable type).
        target: The item to search for.

    Returns:
        int: Index of target if found, else -1.

    Note:
        `items` must be sorted in ascending order.
    """
    left, right = 0, len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ----------- Test Cases -----------

def test_linear_search():
    print("=" * 60)
    print("LINEAR SEARCH TEST CASES")
    print("=" * 60)
    
    # Test 1: Search for existing item
    print("\nTest 1: Search for existing item in list")
    print("-" * 60)
    items = ["Box", "Pallet", "Crate", "Drum"]
    target1 = "Crate"
    result1 = linear_search(items, target1)
    print(f"Items: {items}")
    print(f"Target: '{target1}'")
    print(f"Result: Index {result1}")
    assert result1 == 2
    print("✓ Test 1 PASSED - Found 'Crate' at index 2")
    
    # Test 2: Search for non-existing item
    print("\nTest 2: Search for non-existing item")
    print("-" * 60)
    target2 = "Forklift"
    result2 = linear_search(items, target2)
    print(f"Items: {items}")
    print(f"Target: '{target2}'")
    print(f"Result: Index {result2} (not found)")
    assert result2 == -1
    print("✓ Test 2 PASSED - 'Forklift' not found, returned -1")
    
    # Test 3: Search in empty list
    print("\nTest 3: Search in empty list")
    print("-" * 60)
    empty_items = []
    target3 = "Drum"
    result3 = linear_search(empty_items, target3)
    print(f"Items: {empty_items}")
    print(f"Target: '{target3}'")
    print(f"Result: Index {result3} (not found)")
    assert result3 == -1
    print("✓ Test 3 PASSED - Empty list search returned -1")
    
    print("\n" + "=" * 60)
    print("ALL LINEAR SEARCH TESTS PASSED ✓")
    print("=" * 60)

def test_binary_search():
    print("\n" + "=" * 60)
    print("BINARY SEARCH TEST CASES")
    print("=" * 60)
    
    # Test 1: Search for first item
    print("\nTest 1: Search for first item in sorted list")
    print("-" * 60)
    items = ["Bolts", "Boxes", "Cables", "Drills", "Wrenches"]  # Sorted
    target1 = "Bolts"
    result1 = binary_search(items, target1)
    print(f"Items (sorted): {items}")
    print(f"Target: '{target1}'")
    print(f"Result: Index {result1}")
    assert result1 == 0
    print("✓ Test 1 PASSED - Found 'Bolts' at index 0")
    
    # Test 2: Search for middle item
    print("\nTest 2: Search for middle item in sorted list")
    print("-" * 60)
    target2 = "Drills"
    result2 = binary_search(items, target2)
    print(f"Items (sorted): {items}")
    print(f"Target: '{target2}'")
    print(f"Result: Index {result2}")
    assert result2 == 3
    print("✓ Test 2 PASSED - Found 'Drills' at index 3")
    
    # Test 3: Search for non-existing item
    print("\nTest 3: Search for non-existing item")
    print("-" * 60)
    target3 = "Screws"
    result3 = binary_search(items, target3)
    print(f"Items (sorted): {items}")
    print(f"Target: '{target3}'")
    print(f"Result: Index {result3} (not found)")
    assert result3 == -1
    print("✓ Test 3 PASSED - 'Screws' not found, returned -1")
    
    # Test 4: Search in empty list
    print("\nTest 4: Search in empty list")
    print("-" * 60)
    empty_items = []
    target4 = "Cables"
    result4 = binary_search(empty_items, target4)
    print(f"Items: {empty_items}")
    print(f"Target: '{target4}'")
    print(f"Result: Index {result4} (not found)")
    assert result4 == -1
    print("✓ Test 4 PASSED - Empty list search returned -1")
    
    print("\n" + "=" * 60)
    print("ALL BINARY SEARCH TESTS PASSED ✓")
    print("=" * 60)

if __name__ == "__main__":
    test_linear_search()
    test_binary_search()
