 def brokenCalc(self, startValue, target):
        if startValue > target: return startValue - target
        if startValue == target: return 0
        if target % 2 == 0:
            return self.brokenCalc(startValue, target//2) + 1
        else:
            return self.brokenCalc(startValue, target + 1) + 1