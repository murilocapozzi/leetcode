class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        
        luckyNumbers = []
        maxColumns = []
        m = len(matrix)
        n = len(matrix[0])

        # Itera pela matriz para guardar os máximos de cada coluna
        for j in range(n):
            maxColumn = -1
            for i in range(m):
                maxColumn = max(maxColumn, matrix[i][j])
            maxColumns.append(maxColumn)

        # Itera pelas linhas da matriz
        # Descobre o valor mínimo e, pelo index dele
        # Compara com o valor máximo da coluna de mesmo index
        # Se for igual, é um número da sorte
        for i in range(m):
            
            minRow = min(matrix[i])

            if maxColumns[matrix[i].index(minRow)] == minRow:
                luckyNumbers.append(minRow)

        return luckyNumbers