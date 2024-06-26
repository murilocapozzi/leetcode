class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i = 0
        j = len(s) - 1
        output = list(s)
        vowels = "aAeEiIoOuU"

        while i < j:

            while i < j and vowels.find(output[i]) == -1:
                i += 1

            while i < j and vowels.find(output[j]) == -1:
                j -= 1

            output[i], output[j] = output[j], output[i]

            i += 1
            j -= 1

        return "".join(output)