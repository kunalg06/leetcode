'''Given an array, move all 0s to the end while maintaining the order of non-zero elements.

Example

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]'''

def move_zeros_to_end(arr): 
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != 0: #why do we need to check for non-zero elements? Because we want to keep the order of non-zero elements intact and move all zeros to the end. If we find a non-zero element at index i, we simply move the pointer i forward to check the next element.
            i += 1
        elif arr[j] == 0: #why do we need to check for zero elements? Because we want to move all zeros to the end. If we find a zero element at index j, we simply move the pointer j backward to check the previous element.
            j -= 1 
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return arr
