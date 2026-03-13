class Solution(object):
    def lengthOfLastWord(self, s):
        tamanho = len(s) - 1
        print(tamanho)

        while tamanho >= 0 and s[tamanho] == ' ':
            tamanho -= 1

        ultima = tamanho

        while tamanho >= 0 and s[tamanho] != ' ':
            tamanho -= 1
        
        return ultima - tamanho
        