class Solution:
    def compress(self, chars: list[str]) -> int:

        count = 1
        length = len(chars)

        if length == 1:
            return 1

        # Cria uma cópia intacta de chars, já que precisamos mudar a própria como pede o enunciado
        copy_chars = chars.copy()
        chars.clear()
        i = 1

        while i < length:

            # Contabiliza quantas vezes aparece o caracter
            if copy_chars[i-1] == copy_chars[i]:
                count += 1
            # Ao ver um caracter diferente do anterior, quebra o count e insere no chars a letra
            # Se count for maior que 1, deve ser inserido
            # Obs: Deve ser inserido caracter por caracter do dígito, por isso o strip(), que retorna uma lista, por isso também o extend
            else:
                chars.append(copy_chars[i-1])
                if count > 1:
                    chars.extend(list(str(count).strip()))
                count = 1
                
            i += 1
            
            if i == length:
                chars.append(copy_chars[i-1])
                if count > 1:
                    chars.extend(list(str(count).strip()))

        return len(chars)

        