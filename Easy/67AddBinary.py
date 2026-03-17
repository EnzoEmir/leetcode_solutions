# class Solution(object):
#     def addBinary(self, a, b):
#         resultado = []
#         resto = 0

#         ultimo_a = len(a) - 1
#         ultimo_b = len(b) - 1

#         while ultimo_a >= 0 or ultimo_b >= 0 or resto:
#             soma = resto

#             if ultimo_a >= 0:
#                 soma += int(a[ultimo_a])
#                 ultimo_a -= 1

#             if ultimo_b >= 0:
#                 soma += int(b[ultimo_b])
#                 ultimo_b -= 1

#             resultado.append(str(soma % 2))

#             resto = soma // 2
        
#         return "".join(reversed(resultado))
        
class Solution(object):
    def addBinary(self, a, b):
        ab = int(a,2)
        bb = int(b,2)

        return format(ab + bb, 'b')
        