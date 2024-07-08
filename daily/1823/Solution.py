from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        friends = deque(i+1 for i in range(n))
        counter = 1

        while len(friends) > 1:
            print(friends)
            friend = friends.popleft()
            
            if counter >= k:
                counter = 1
            else:
                friends.append(friend)
                counter += 1

        return friends[0]
        