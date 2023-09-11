import math
class Solution:
    def countSquares(self, N):
        a=math.sqrt(N)
        if a==int(a):
            return int(a-1)
        return int(a)
