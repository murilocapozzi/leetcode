class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:

        # Ordena os dois vetores, já que o aluno da posição i irá se adequar melhor na cadeira i
        seats = sorted(seats)
        students = sorted(students)

        moves = 0
        # Soma o valor dos movimentos individuais
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])

        return moves
        