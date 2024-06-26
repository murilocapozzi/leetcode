class Solution:        
    def splitBrackets(self, s: str, start: int) -> str:
        brackets = 1
        end = start
        
        # Conta a quantidade de colchetes
        # Incrementa ao achar um [
        # Decrementa ao achar um ]
        # Quando o contador é zero, todos abriram e fecharam, logo é possível retornar o que estava dentro do primeiro colchete
        while end < len(s):
            if s[end] == ']': brackets -= 1
            elif s[end] == '[': brackets += 1
            if brackets == 0: break
            end += 1
        
        # Retorna a posição do último, para incrementar no index de onde foi chamado
        return end

    def repeatStr(self, s:str, n: int) -> str:
        ans = ''
        i = 0
        
        while i < len(s):
        # Itera sob o bloco desejado para repetição, a fim de descobrir se existem outros blocos a quebrar

            if s[i].isdigit():
            # Se for um número, é um novo bloco, descobre que bloco é esse e envia para decodeString, como se fosse reiniciar o problema mas sendo menor
                j = self.splitBrackets(s, i+1)
                ans += self.decodeString(s[i:j])
                i = j
            elif s[i].isalpha():
            # Caracteres individuais são armazenados diretamente
                ans += s[i]
            i += 1

        return ans * n

    def decodeString(self, s: str) -> str:
        ans = ''
        i = 0
        
        while i < len(s):
            
            if s[i].isdigit():
            # Ao encontrar um número na string, itera até que não seja um número
                n = s[i]
                i += 1
                
                while i < len(s) and s[i].isdigit():
                    n += s[i]
                    i += 1

                # Pela lógica do exercício, após um número, começa um bloco de colchetes a se repetir
                # Chama splitBrackets para saber o que irá repetir
                j = self.splitBrackets(s, i+1)
                # Sabendo o bloco e a quantidade, chama repeatStr
                ans += self.repeatStr(s[i+1: j], int(n))
                i = j
                
            # Caracteres individuais são armazenados diretamente
            elif s[i].isalpha(): ans += s[i]
            
            i += 1

        return ans
