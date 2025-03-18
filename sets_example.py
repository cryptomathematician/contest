class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion( a, b):
        # code here
        return len(set(a + b))
    

    print(findUnion( [1, 2, 3, 4, 5],[1, 2, 3]))