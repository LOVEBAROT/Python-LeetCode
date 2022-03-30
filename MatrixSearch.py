class Solution(object):
       def searchMatrix(self, matrix, target):
            list = []
            for i in matrix:
               list.extend(i)
            if target in list:
                return True
            else:
                return False