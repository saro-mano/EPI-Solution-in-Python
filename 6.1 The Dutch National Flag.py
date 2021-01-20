class Solution:
    def sort(arr):
        left = 0
        right = len(arr)-1
        cur = 0

        while cur <= right:
            if arr[cur] == 2:
                arr[cur],arr[right] = arr[right],arr[cur]
                right -= 1
            
            if arr[cur] == 1:
                cur += 1
            
            if arr[cur] == 0:
                arr[cur],arr[left] = arr[left],arr[cur]
                cur += 1
                left += 1
        
        return arr


print(Solution.sort([0,1,2,0,2,1,1]))