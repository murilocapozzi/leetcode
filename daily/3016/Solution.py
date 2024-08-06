from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        mapping = {}
        i = 0
        push = 1
        total = 0

        for letter in sorted({**Counter(word)}.items(), key=lambda x: x[1], reverse=True):
            if i >= 8:
                push += 1
                i = 0
            mapping[letter[0]] = push
            i += 1
            
        for letter in word: total += mapping[letter]

        return total
