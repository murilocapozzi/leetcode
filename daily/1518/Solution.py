class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        # Inicia o exercício tomando as águas
        emptyBottles = numBottles
        ans = numBottles

        # Enquanto houver número suficiente de garrafas vazias para trocar por novas
        while emptyBottles >= numExchange:
            
            # 'exchanges' é a quantidade de novas garrafas que pode-se tomar, adiciona a 'ans'
            exchanges = (emptyBottles // numExchange)
            ans += exchanges
            
            # Para saber quantas garrafas vazias temos, pegamos quantas sobraram da divisão inteira, o resto
            # E adiciona as novas, já bebidas
            emptyBottles = (emptyBottles % numExchange) + exchanges

        return ans