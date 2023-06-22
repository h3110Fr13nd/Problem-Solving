from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        sum = 0
        min = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] > min + fee:
                sum += prices[i] - min - fee
                min = prices[i] - fee
        return sum
        

def test():
    solution = Solution()
    assert solution.maxProfit([1,3,2,8,4,9],2) == 8, "Wrong Answer"
    assert solution.maxProfit([1,3,7,5,10,3],3) == 6, "Wrong Answer"


if __name__ == "__main__":
    test()
    print("Passed All Testcases")

