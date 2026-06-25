'''Given an array, move all 0s to the end while maintaining the order of non-zero elements.

Example

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]'''

def move_zeros_to_end(arr): 
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != 0:
            i += 1
        elif arr[j] == 0:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return arr
