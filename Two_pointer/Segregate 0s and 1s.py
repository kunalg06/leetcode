'''2. Segregate 0s and 1s

Given an array of only 0s and 1s, place all 0s on the left and 1s on the right.

Input: [0,1,0,1,1,0]
Output: [0,0,0,1,1,1]'''

def segregate0and1(arr):
    i = 0
    j= len(arr) -1
    while i<j:
        if arr[i] != 1:
            i+=1
        elif arr[j] != 0:
            j-=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
    return arr

arr = [0,1,0,1,1,0]
print(segregate0and1(arr))