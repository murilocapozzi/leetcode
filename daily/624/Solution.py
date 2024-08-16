class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        
        maxDist = 0
        minGlobal = arrays[0][0]
        maxGlobal = arrays[0][-1]

        for i in range(1, len(arrays)):

            maxDist = max(maxDist, abs(maxGlobal - arrays[i][0]), abs(arrays[i][-1] - minGlobal))

            minGlobal = min(minGlobal, arrays[i][0])

            maxGlobal = max(maxGlobal, arrays[i][-1])


        return maxDist