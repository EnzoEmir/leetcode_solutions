class Solution(object):
    def mySqrt(self, x):
        esquerda = 0 
        direita = x
        res = 0

        while esquerda <= direita:
            metade = (esquerda + direita) // 2

            if metade * metade > x:
                direita = metade - 1
            
            elif metade *  metade < x:
                esquerda = metade + 1
                res = metade
            else:
                return metade

        return res