class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        Number_to_remove = k
        for current_element in num:
            while Number_to_remove and stack and stack[-1] > current_element:
                stack.pop()
                Number_to_remove = Number_to_remove - 1
            stack.append(current_element)
        answer = "".join(stack[0:len(num)-k]).lstrip("0")
        if len(answer):
            return answer
        else:
            return "0"
                