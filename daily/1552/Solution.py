class Solution(object):
    def maxDistance(self, position: list[int], m: int) -> int:
        position = sorted(position)
        
        low, high = 1, (position[-1] - position[0]) // (m - 1)
        dist = 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self.canDistributeMBalls(position, mid, m):
                dist = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return dist
    
    def canDistributeMBalls(self, arr, dist, balls):
        countBalls = 1
        lastPlaced = arr[0]
        
        for i in range(1, len(arr)):
            
            if arr[i] - lastPlaced >= dist:
                countBalls += 1
                lastPlaced = arr[i]
                
            if countBalls == balls:
                return True
            
        return False