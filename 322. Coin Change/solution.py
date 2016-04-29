class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        step = {}
        step[0] = 0
        queue = [0]
        while queue:
            curr = queue.pop(0)
            level = step[curr]
            if curr == amount:
                return level
            for coin in coins:
                if curr + coin > amount:
                    continue
                if (curr + coin) not in step:
                    queue.append(curr+coin)
                    step[curr+coin] = level + 1
        return -1