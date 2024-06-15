class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        

        # PRECISA-SE DE OTIMIZAÇÃO!


        longestPath = 0
        i = 0

        while i < len(nums):

            # Novo caminho para explorar começando em i
            currentPath = 1
            # Usos de flips, não pode ultrapassar k por caminho
            flips = 0
            last_flip = -1
            last_following_ones_by_j = 0
            
            while i < len(nums) and nums[i] == 0: i += 1

            if i >= len(nums):
                currentPath = 0
                before_i = i - 1
                while before_i >= 0 and nums[before_i] == 0 and flips < k:
                    flips += 1
                    currentPath += 1
                    before_i -= 1

                longestPath = max(currentPath, longestPath)
                break


            j = i + 1
            while j < len(nums) and nums[j] == 1:
                j += 1
                currentPath += 1
            
            last_following_ones_by_j = j


            while j < len(nums):

                # Se ainda houver flips, tentará substituir para acrescentar no caminho
                if nums[j] == 0 and flips >= k: break
                if nums[j] == 0 and flips < k:
                    flips += 1
                    last_flip = j

                currentPath += 1
                j += 1
            
            # Caso tenha acabado o array (j == len(nums)) e flips < k, tenta criar caminho de i - 1 para trás
            before_i = i - 1
            while before_i >= 0 and nums[before_i] == 0 and flips < k:
                flips += 1
                currentPath += 1
                before_i -= 1

            longestPath = max(currentPath, longestPath)

            if flips == 0 or last_flip == j + k:
                i = j + k
            else:
                i = last_following_ones_by_j

        return longestPath
    

nums = [1,0,0,1,0,0,1,0,1,1, 1,1,0,1,1,1,1,0,1,1, 1,1,1,1,0,1,1,1,0,0, 1,1,1,0,0,1,0,1,0,0, 1,0,0,1,1]
k = 9

output = Solution().longestOnes(nums, k)

print(output)