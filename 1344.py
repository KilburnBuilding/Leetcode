# -*- coding: utf-8 -*-


class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        eachAngle = 360 * 1.0 / 60 
        hourDict = dict()
        for i in range(1, 12):
            hourDict[i] = 5 * i
        hourDict[12] = 0

        hourMinute = hourDict[hour] + minutes * (1 / 60) * 5

        if minutes >= hourMinute:
            angel = (minutes - (hourDict[hour] + 5 * minutes * (1 / 60))) * eachAngle
        else:
            angel = ((hourDict[hour] + 5 * minutes * (1 / 60)) - minutes) * eachAngle

        supplementAngel = 360 - angel

        if supplementAngel > angel:
            return angel
        else:
            return supplementAngel


if __name__ == "__main__":
    hour = 6
    minutes = 5
    S = Solution()
    print(S.angleClock(hour, minutes))