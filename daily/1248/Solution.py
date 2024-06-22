class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:

        start = count = totalCount = 0

        for end in range(len(nums)):

            if nums[end] % 2: # Se acha um primo, diminui de k e zera a contagem
                k -= 1
                count = 0
                print(f'count=0, end={end}, k={k}')
            while not k: # Enquanto não acha um outro primo com k = 0
                k += (nums[start] % 2)
                count += 1
                print(f'\tcount={count}, start={start} end={end}, k={k}')
                start += 1

            # Enquanto houver apenas pares pela frente, count não irá zerar
            # E o total será agregado das possibilidades de subarrays já cheia (como no exemplo 3, na qual encontra-se 4 substrings até o k ímpar, e soma-se 4 a cada par para frente)
            totalCount += count
            
        return totalCount