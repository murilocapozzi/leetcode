class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        
        highest = altitude = 0

        # Inicia-se na altitude 0, soma a cada passo e compara se está na maior altitude
        for step in gain:
            altitude += step
            highest = max(highest, altitude)

        return highest