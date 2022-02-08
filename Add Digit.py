class Solution(object):
    def addDigits(self,num):
        result = 0
        global ans
        if num > 0:
            res = [int(x) for x in str(num)]
            for i in res:
                result +=  i
            if(1 <= int(result) <= 9):
                ans = result
            else:
                self.addDigits(result)
        else:
            return 0
        return ans 

       
        