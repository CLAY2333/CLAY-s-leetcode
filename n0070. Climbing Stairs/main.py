// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    D = {'test': -999}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        D=self.D
        if str(n) in D.keys():
            return D[str(n)]
        if(n==1 or n==0):
            return 1
        if(n==2):
            return 2
        if(n==3):
            return 3
        D[str(n)]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return D[str(n)]
