class Solution:
    
    def getSecondLargest(self, arr):
        n=len(arr)
        
        if n < 2:
            return -1
        
        max = smax = float('-inf')
        
        for i in arr:
            if i > max:
                smax=max
                max=i
            elif i > smax and i != max:
                smax = i
                
        
        if smax == float('-inf'):
            return -1
        else:
            return smax
