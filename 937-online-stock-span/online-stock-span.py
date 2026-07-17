class StockSpanner(object):

    def __init__(self):
        self.stk=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        #Solution says we need to use monotonically decrasing stack
        span = 1
        while self.stk and self.stk[-1][0]<=price:
            _,e=self.stk.pop()
            span+=e
        self.stk.append((price,span))
        return span
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)