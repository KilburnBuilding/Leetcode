class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.list.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        result = self.list.pop(0)
        return result

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        result = self.list[0]
        return result
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        result = False
        if not self.list:
            result = True
        
        return result


if __name__ == "__main__":
    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()