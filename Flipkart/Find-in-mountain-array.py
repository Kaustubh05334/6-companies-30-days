def findInMountainArray(target: int, arr) -> int:
        left,right = 0,arr.length() - 1
        #Find the peak index
        while (left < right):
            mid = left + (right - left) // 2
            if arr.get(mid) < arr.get(mid + 1):
                left = mid + 1
            else: 
                right = mid
        
        peak = left
        
        #Binary search on increasing subarray
        left,right = 0,peak
        while (left <= right):
            mid = left + (right - left)// 2
            if arr.get(mid) < target:
                left = mid + 1
            elif arr.get(mid) > target: 
                right = mid - 1
            else: 
                return mid
        
        #Binary search on decreasing subarray
        left = peak;
        right = arr.length() - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if arr.get(mid) < target:
                right = mid - 1
            elif arr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        return -1