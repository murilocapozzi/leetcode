class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        
        if m * k > len(bloomDay): return -1
        
        minDay, maxDay = min(bloomDay), max(bloomDay)

        for day in range(minDay, maxDay + 1, 1):
            
            if day not in bloomDay:
                continue

            for i in range(len(bloomDay)):
                if bloomDay[i] == day: bloomDay[i] = 'x'
                    
            substrings = []
            i = 0
            while i < len(bloomDay):
                
                while i < len(bloomDay) and bloomDay[i] != 'x': i += 1
                    
                if i >= len(bloomDay) or bloomDay[i] != 'x': break
                    
                j = i
                while j < len(bloomDay) and bloomDay[j] == 'x':
                    if j - i + 1 >= k:
                        break
                    j += 1
                
                if j < len(bloomDay) and bloomDay[j] == 'x':
                    substrings.append(j - i + 1)
                    i = j + 1
                else:
                    substrings.append(j - i)
                    i = j
                
            if len(substrings) >= m:
                bouquets = 0
                for adjFlowers in substrings:
                    if adjFlowers >= k:
                        bouquets += 1
                        
                if bouquets >= m:
                    return day
            
        return -1
    
   
bloomDay = [1,10,2,9,3,8,4,7,5,6]
m = 4
k = 2



output = Solution().minDays(bloomDay, m, k)

print(output)