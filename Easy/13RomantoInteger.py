class Solution(object):
    def romanToInt(self, s):
        valores = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        valor_anterior = 0

        for x in reversed(s):
            valor_atual = valores[x]

            if valor_atual < valor_anterior:
                total = total - valor_atual

            else:
                total = total +valor_atual

            valor_anterior = valor_atual
        
        return total
    