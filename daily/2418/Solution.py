class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        
        people = [(names[i], heights[i]) for i in range(len(names))]

        people = sorted(people, key=lambda x: x[1], reverse=True)

        return [name for name, _ in people]