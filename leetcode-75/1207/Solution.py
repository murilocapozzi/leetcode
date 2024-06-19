class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        uniqueArr = set(arr)
        lenght = len(set(arr))
        
        occurrences = {}
        
        for num in arr:
            if num in occurrences:
                occurrences[num] += 1
            else:
                occurrences[num] = 1
                
        quantity = []      
        
        for key in occurrences:
            
            if occurrences[key] in quantity:
                return False
            
            quantity.append(occurrences[key])
            
        print(occurrences)
        print(quantity)
            
        return True
    
arr = [1, 2]

output = Solution().uniqueOccurrences(arr)

print(output)