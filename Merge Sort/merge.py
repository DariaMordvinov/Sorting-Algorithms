def merge(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Recursive call on each half
        merge(left)
        merge(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            # The value from the left is lesser
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            # The value from the right half is bigger
            else:
                list[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        # If there is still values in the left half, we should add all of them
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        # If there is still values in the right half, we should add all of them
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

