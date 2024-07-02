class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        # Ordena as listas para manter "sincronia" enquanto itera sobre eles
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        ans = []
        
        while i < len(nums1) and j < len(nums2):
            
            # Se não for igual, determina qual ponteiro irá andar
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                # Sendo igual, é elemento da interseção, insere na resposta e anda com os dois ponteiros
                ans.append(nums1[i])
                i += 1
                j += 1
        
        return ans
        