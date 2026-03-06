# class Solution(object):
#     def isValid(self, s):
#         abre = ['(','[', '{']
#         fecha = [')',']', '}']
#         pilha = []
        
#         for x in range(len(s)):
#             caractere = s[x]
#             if caractere in abre:
#                 pilha.append(caractere)
#             else:
#                 if not pilha:
#                     return False

#                 ultimo_pilha = pilha.pop()
#                 pos_fecha = fecha.index(caractere)

#                 if ultimo_pilha != abre[pos_fecha]:
#                     return False 
            
#         return len(pilha) == 0



    
class Solution(object):
    def isValid(self, s):
        # Hash map
        pares = {')': '(', ']': '[', '}': '{'}
        pilha = []
        
        for x in s:
            if x in pares:
                # if em uma linha
                ultimo_pilha = pilha.pop() if pilha else 'X'

                if pares[x] != ultimo_pilha:
                    return False

            else:
                pilha.append(x)
            
        return len(pilha) == 0

