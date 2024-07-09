class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        
        ans = totalTime = 0
        n = len(customers)

        for i in range(n):

            if totalTime < customers[i][0]:
                totalTime = customers[i][0]

            totalTime += customers[i][1]
            ans += (totalTime - customers[i][0])

        return ans / n