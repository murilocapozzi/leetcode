class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        minValue, maxValue = min(arr), max(arr)
        print(set(arr))
        
        occurrences = [0] * (maxValue - minValue + 1)
        
        for num in arr:
            occurrences[num + minValue - maxValue] += 1
            
        print(occurrences)
        
        quantity = [[]] * (maxValue - minValue + 1)
        
        for i in range(len(occurrences)):
            
            quantity[occurrences[i]].append(i)
            
        print(quantity)
            
            
        return False
    
arr = [1,2]

output = Solution().uniqueOccurrences(arr)