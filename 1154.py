# -*- coding: utf-8 -*-
import datetime


class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        strYear = date.split('-')[0]
        strDate = '%s-%s-%s' % (strYear, '01', '01')
        d1 = datetime.datetime.strptime(strDate, '%Y-%m-%d')
        d2 = datetime.datetime.strptime(date, '%Y-%m-%d')
        diffDays = d2 - d1
        return diffDays.days + 1


if __name__ == "__main__":
    S = Solution()
    print(S.dayOfYear('2020-01-09'))
        