# -*- coding: utf-8 -*-


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        day_cost = [0 for i in range(0, 366)]

        for index, val in enumerate(days):
            if val > 1:
                A = day_cost[val - 1] + costs[0]
            else:
                A = day_cost[0] + costs[0]
            if val > 7:
                B = day_cost[val - 7] + costs[1]
            else:
                B = day_cost[0] + costs[1]
            if val > 30:
                C = day_cost[val - 30] + costs[2]
            else:
                C = day_cost[0] + costs[2]
            day_cost[val] = min(A, B, C)

            temp_record = val
            while temp_record < days[-1] and temp_record < days[index + 1]:
                day_cost[temp_record] = day_cost[val]
                temp_record += 1

        return day_cost[days[-1]]


# class Solution(object):
#     def mincostTickets(self, days, costs):
#         """
#         :type days: List[int]
#         :type costs: List[int]
#         :rtype: int
#         """
#         dayCosts = [0]*366

#         for i, day in enumerate(days):
#             dayCosts[day] = min(  dayCosts[day-1] + costs[0], dayCosts[max(0,day-7)] + costs[1], dayCosts[max(0,day-30)] + costs[2])
#             j = day + 1
#             print('i:%s, day:%s' % (i, day))
#             while j < days[-1] and j < days[i + 1]:
#                 dayCosts[j] = dayCosts[day]
#                 j += 1
        
#         return dayCosts[days[-1]]


if __name__ == "__main__":
    S = Solution()
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    print(S.mincostTickets(days, costs))


"""
In a country popular for train travel, you have planned some train travelling one year in advance.  
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.
"""