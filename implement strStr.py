class Solution(object):
    def strStr(self, haystack, needle):
        if (len(haystack) == 0) and (len(needle) == 0):
            return 0
        elif (len(needle) > len(haystack)):
            return -1
        StrPos = 0
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                StrPos = i
                break
            else:
                StrPos = -1
        return StrPos
        