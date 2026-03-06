class Solution(object):
    def longestCommonPrefix(self, strs):
        palavra_guardada = ""
        palavra_base = strs[0]

        for letra in range(len(palavra_base)):
            letra_comparar = palavra_base[letra] 

            for palavra in strs:
                if  letra == len(palavra) or palavra[letra] != letra_comparar:
                    return palavra_guardada
                
            palavra_guardada = palavra_guardada + letra_comparar

        return palavra_guardada
    