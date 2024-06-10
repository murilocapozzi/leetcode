class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        before_i_product = [1 for i in range(n)]
        after_i_product = [1 for i in range(n)]


        # Preenche o vetor BEFORE com os produtos antes do i

        i = 1
        while i < n:
            before_i_product[i] = before_i_product[i - 1] * nums[i - 1]
            i += 1


        # Preenche o vetor AFTER com os produtos depois do i

        i = n - 2
        while i >= 0:
            after_i_product[i] = after_i_product[i + 1] * nums[i + 1]
            i -= 1


        output = [1 for _ in range(n)]


        # Realiza então o produto dos anteriores com os posteriores, excluindo si mesmo
        for i in range(n):
            output[i] = before_i_product[i] * after_i_product[i]

        return output
        