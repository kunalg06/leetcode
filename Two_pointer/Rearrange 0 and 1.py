'''
Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.
- https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
Examples :

Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1].
Input: arr[] = [1, 1]
Output: [1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1]
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 1

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
'''

def segregate0and1(arr):
        # code here
        i = 0
        j = len(arr) - 1
        while (i<j):
        
            if arr[i] == 0:#why do we need to check for zero elements? Because we want to move all zeros to the left. If we find a zero element at index i, we simply move the pointer i forward to check the next element.
                i+=1
            elif arr[j] == 1:#why do we need to check for one elements? Because we want to move all ones to the right. If we find a one element at index j, we simply move the pointer j backward to check the previous element.
                j-=1
            elif arr[i] == 1 and arr[j] == 0: #if we find a one element at index i and a zero element at index j, we swap them to move the zero to the left and the one to the right. After swapping, we move both pointers i and j towards each other to continue checking the next elements.   
                arr[i], arr[j] = arr[j], arr[i] 
                i+=1
                j-=1    
        return arr
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(segregate0and1(arr))
