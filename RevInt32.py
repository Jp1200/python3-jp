class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if (x >= 2**31-1 or x<= -2**31 ): return 0

        if (x<0):
            x = x * -1
            negative = True


        stx = str(x)
        rstx  = []
        index = len(stx)
        while (index > 0):
            rstx += stx[index -1]
            index = index -1
        emp = ''
        ans = emp.join(rstx)
        ans = int(ans)
        if ans >= 2**31-1 or ans <= -2*31: return 0
        if (negative):
            ans = ans*-1
            return ans
        else:
            return ans
