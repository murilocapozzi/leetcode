class Solution:

    def getProfit(self, cp: list[tuple]) -> int:
        return cp[0]

    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        
        cp = []

        for i in range(len(profits)):
            cp.append((profits[i], capital[i]))

        cp = sorted(cp, key=self.getProfit, reverse=True)
        
        projects = 0
        i = 0
        while i < len(cp):

            if len(cp) > 0 and w >= cp[i][1]:
                w += cp[i][0]
                cp.pop(i)
                projects += 1
                if projects < k:
                    i = 0
                else:
                    break
            else:
                i += 1

        return w
    
k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]

output = Solution().findMaximizedCapital(k, w, profits, capital)

print(output)