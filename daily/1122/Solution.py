class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        quantityAppearArr1 = {}
        output = []

        # Descobre os valores distintos de arr1 e os ordena
        notIncluded = sorted([num for num in arr1 if num not in arr2])
        # Retira de arr1 os valores distintos, afim de não contabilizá-los em quantityAppearArr1
        arr1 = [num for num in arr1 if num not in notIncluded]


        # Preenche o quantityAppearArr1 com a quantidade de vezes que cada valor de arr1 aparece
        for num in arr1:
            if num in quantityAppearArr1:
                quantityAppearArr1[num] += 1
            else:
                quantityAppearArr1[num] = 1


        # Preenche o output na ordem de arr2, apenas repetindo pela quantidade de vezes que aparece em arr1
        for item in arr2:
            for _ in range(quantityAppearArr1[item]):
                output.append(item)

        # Junta output com notIncluded
        output.extend(notIncluded)

        return output