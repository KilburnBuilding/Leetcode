# -*- coding: utf-8 -*-


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.result = list()
    
    def halfSearch(self, num, left, right):
        if left == right:
            if num >= self.result[left]:
                self.result.insert(left + 1, num)
            else:
                self.result.insert(left, num)
            
            return 

        half_value = int((left + right) / 2)
        if self.result[half_value] > num:
            self.halfSearch(num, left, half_value)
        else:
            self.halfSearch(num, half_value + 1, right)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num or num == 0:
            if not self.result:
                self.result.append(num)
            else:
                self.halfSearch(num, 0, self.length - 1)
            self.length = len(self.result)

    def findMedian(self):
        """
        :rtype: float
        """
        print(self.result)
        if self.length % 2 != 0:
            half_index = int(self.length / 2)
            return self.result[half_index]
        else:
            half_index = int(self.length / 2)
            return (self.result[half_index] + self.result[half_index - 1]) / 2
        

if __name__ == "__main__":
    S = MedianFinder()
    S.addNum("")
    S.addNum(1)
    S.addNum(2)
    print(S.findMedian())
    S.addNum("")
    S.addNum(3)
    # print(S.findMedian())
    # S.addNum("")
    # print(S.findMedian())

     
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()