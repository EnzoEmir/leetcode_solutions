class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        primeiro = 1
        segundo = 2

        for x in range(3, n + 1):
            novo = primeiro + segundo
            primeiro = segundo
            segundo = novo
        return novo
    