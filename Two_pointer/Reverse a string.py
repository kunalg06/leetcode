'''
Reverse a character array in-place.

Input: ['h','e','l','l','o']
Output: ['o','l','l','e','h']   
'''

def reverse_string(s):
    i = 0
    j = len(s) - 1
    while (i<j):
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
    return s