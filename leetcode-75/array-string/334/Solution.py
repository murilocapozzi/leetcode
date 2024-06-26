from numpy import inf

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        first, second = inf, inf

        for third in nums:

            # Garante-se que first e second estão preenchidos e, mesmo que no contexto 
            # dos indices não faça sentido, a lógica permaneceu e a tripla existe
            if second < third: 
                return True

            # Garante que o primeiro seja o menor (até i) visto
            # Isso permite a visualizacao de triplas verdadeiras na frente de falsas triplas
            # Logo, quando confere second < third, é porque o first foi preenchido e, mesmo que esteja a frente
            # do second, existe um numero menor que second mas maior que o first, que garante e tripla
            if third <= first:
                first = third
            # Atualiza o second ao ver um numero maior que first
            else:
                second = third

        return False
        