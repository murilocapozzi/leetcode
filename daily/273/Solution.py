class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0: return 'Zero'
        
        self.num = num
        BILLION = 1000000000
        MILLION = 1000000
        THOUSAND = 1000
        HUNDRED = 100
        TEN = 10
        dec = [None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        below20 = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        numbers = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

        output = []

        def getRepresentation():

            def getHundreds(magnitude):
                if self.num == 0: return ''
                
                output = ''
                output = numbers[self.num // (magnitude * HUNDRED)]
                self.num -= (self.num // (magnitude * HUNDRED)) * (magnitude * HUNDRED)
                
                return output

            def getTens(magnitude):
                if self.num == 0: return ''
                
                output = ''
                if 10 <= self.num // magnitude < 20:
                    self.num -= (self.num // (magnitude * TEN)) * (magnitude * TEN)
                    output += below20[self.num // magnitude]
                    self.num -= (self.num // magnitude) * magnitude
                elif self.num // magnitude >= 20:
                    output += dec[self.num // (magnitude * TEN)]
                    self.num -= (self.num // (magnitude * TEN)) * (magnitude * TEN)
                
                return output
                
            def getOnes(magnitude):
                if self.num == 0: return ''
                
                output = ''
                output = numbers[self.num // magnitude]
                self.num -= (self.num // magnitude) * magnitude
                
                return output
                
            output = ''

            if self.num >= BILLION:
                output += getOnes(BILLION) + ' Billion'
                
            elif self.num >= MILLION:
                hundreds = getHundreds(MILLION)
                tens = getTens(MILLION)
                ones = getOnes(MILLION)
                
                if hundreds != '': output += hundreds + ' Hundred'
                if tens != '': output += ' ' + tens
                if ones != '':output += ' ' + ones
                if output != '': output += ' Million'

            elif self.num >= THOUSAND:
                hundreds = getHundreds(THOUSAND)
                tens = getTens(THOUSAND)
                ones = getOnes(THOUSAND)
                
                if hundreds != '': output += hundreds + ' Hundred'
                if tens != '': output += ' ' + tens
                if ones != '': output += ' ' + ones

                if output != '': output += ' Thousand'
                
            else:
                hundreds = getHundreds(1)
                tens = getTens(1)
                ones = getOnes(1)
                
                if hundreds != '': output += hundreds + ' Hundred'
                if tens != '': output += ' ' + tens
                if ones != '': output += ' ' + ones
                
            return output

        while self.num > 0:
            output.append(getRepresentation().strip())

        return ' '.join(output)