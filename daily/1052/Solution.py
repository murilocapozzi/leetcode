class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:

        init_s = window_s = 0
        n = len(customers)

        # Soma a satisfação inicial para quando o dono não está 'grumpy'
        # E inicia a janela deslizantes nos primeiros minutos se o dono está 'grumpy'
        for i in range(n):
            if grumpy[i] == 0:
                init_s += customers[i]
            elif i < minutes:
                window_s += customers[i]
        
        extra_s = window_s

        for i in range(minutes, n):
            # Janela deslizante, vê qual a janela possui a maior satisfação
            # considerando que neste tempo extra o dono está 'grumpy'
            window_s += customers[i] * grumpy[i]
            window_s -= customers[i - minutes] * grumpy[i - minutes]
            extra_s = max(extra_s, window_s)

        return init_s + extra_s