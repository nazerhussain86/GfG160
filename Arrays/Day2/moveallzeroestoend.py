class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        
        count=0
        # for loop will add non zero first 
        for i in range(len(arr)):
            if arr[i] !=0:
                arr[count]=arr[i]
                count+=1
        # this while loop will add zero at end comparing with length of array
        while count < len(arr):
             arr[count]=0
             count+=1
