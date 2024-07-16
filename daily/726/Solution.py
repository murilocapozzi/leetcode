class Solution:

    def countOfAtoms(self, formula: str) -> str:

        formula = formula[::-1] # Inverte a fórmula pois dessa forma a multiplicação fica direta pois os números aparecem primeiro
        atoms = {}
        multiplier = 1
        lastNum = [] # Pilha de números encontrados e ainda não finalizados
        i = 0

        while i < len(formula):

            if formula[i] == '(':
                # Ao ver '(':
                #       Significa que acabou um bloco, tira da pilha o último para atualizar o multiplicador
                if lastNum:
                    multiplier //= lastNum.pop()
                    
            elif formula[i].isdigit():
                # Ao ver um dígito:
                #       Lê a totalidade do número
                #       Se existir um ')' após o número, 
                #               É necessário adicionar na pilha o anterior pois é um novo bloco
                #       Se é um caracter
                #               Será apenas um átomo para aquele número, lê ele e cria ou soma
                num = ''
                while formula[i].isdigit():
                    num += formula[i]
                    i += 1

                if formula[i] == ')':
                    lastNum.append(int(num[::-1]))
                    multiplier *= lastNum[-1]
                else:
                    atom = ''
                    if formula[i].islower():
                        atom = formula[i+1] + formula[i] # Átomos de 2 letras
                        i += 1
                    else:
                        atom = formula[i]

                    if atom in atoms: atoms[atom] += (multiplier * int(num[::-1]))
                    else: atoms[atom] = (multiplier * int(num[::-1]))

            elif formula[i].isalpha():
                # Se for um dígito:
                #       Lê ele e cria ou soma
                atom = ''
                if formula[i].islower(): # Átomos de 2 letras
                    atom = formula[i+1] + formula[i]
                    i += 1
                else: atom = formula[i]

                if atom in atoms: atoms[atom] += multiplier
                else: atoms[atom] = multiplier

            i += 1

        # Ordena alfabeticamente pela sigla
        atoms = dict(sorted(atoms.items()))
        
        # Cria a string em si. Obs: Se o valor for 1, apenas a sigla é posta.
        ans = [key + str(value) if value > 1 else key for key, value in atoms.items()]

        return ''.join(ans)



        