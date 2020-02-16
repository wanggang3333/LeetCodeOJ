class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue =[]
        self.minNum = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.queue == None or self.queue == [] or self.minNum[-1] > x:
            self.minNum.append(x)
        else:
            i = self.minNum[-1]
            self.minNum.append(i)
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop()
        self.minNum.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1] 
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum[-1]
        