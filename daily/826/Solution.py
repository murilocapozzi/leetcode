class Solution:

    # Solução semelhante ao desafio 502. IPO - Maximização de ganhos com restrições de dificuldade e trabalhadores

    def getProfit(self, job):
        return job[1]

    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        
        # Armazena a dificuldade com o respectivo ganho
        jobs = [(difficulty[i], profit[i]) for i in range(len(profit))]

        # Ordena o ganho de forma decrescente
        jobs = sorted(jobs, key=self.getProfit, reverse=True)

        j = 0
        totalProfit = 0

        while j < len(worker):

            for job in jobs:

                # Itera sobre os trabalhos mais proveitosos, se acha um que o trabalhador consegue realizar,
                # atribui-se ao total e busca o próximo trabalhador
                if worker[j] >= job[0]:
                    totalProfit += job[1]
                    break

            j += 1

        return totalProfit