class Solution(object):
    def isPalindrome(self, x):
        texto = str(x)
        tamanho = len(texto)
        i = 0

        while i < tamanho // 2:
            if not texto[i] == texto[-(i+1)]:
                return False
            
            i = i+1
        
        return True
    