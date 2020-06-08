# -*- coding: utf-8 -*-
import heapq


class KthLargest:
    """
    The idea is to ALWAYS maintain a MIN heap with only K elements
    - in this case, the K-the largest element (in the stream)
    - will always be at the root position
    """
    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        
        for num in nums:
            self.add(num) # add elements using the function below
        
    def add(self, val: int):
        heapq.heappush(self.heap, val)
        
        # if after adding the new item causes 
        # the heap size to increase beyond k, 
        # then pop out the smallest element 
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)
            
        return self.heap[0] # the root element


if __name__ == "__main__":
    a = [4, 5, 8, 2]
    k = 3
    K = KthLargest(k, a)
    print(K)
    K.add(3)
    K.add(5)
    K.add(10)
    K.add(9)
    K.add(4)

