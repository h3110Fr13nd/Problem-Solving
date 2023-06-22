from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def cost_min(l):
            return sum(abs(n-l)*c for n,c in zip(nums,cost))

        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left+right)//2
            if cost_min(mid) > cost_min(mid+1):
                left = mid+1
            else:
                right = mid

        return cost_min(left)

        

    







def test():
    solution = Solution()
    print("Expected result: 8, Actual result: ", solution.minCost([1,3,5,2],[2,3,1,14]))
    print("Expected result: 0, Actual result: ", solution.minCost([2,2,2,2,2],[4,2,8,1,3]))
    assert solution.minCost([1,3,5,2],[2,3,1,14]) == 8, "Testcase 1 Failed"
    
    assert solution.minCost([2,2,2,2,2],[4,2,8,1,3]) == 0 , "Testcase 2 Failed"

if __name__ == "__main__":
    test()
    print("Passed All Testcases")


'''
1,2,3,5  2,14,3,1
weighted cost= 1*2 + 2*14 + 3*3 + 5*1 = 2+28+9+5 = 44



sum(2,14,3,1) = 20

18

1

    1:  1-1 = 0 * 2 = 0
    2:  2-1 = 1 * 14 = 14
    3:  3-1 = 2 * 3 = 6
    5:  5-1 = 4 * 1 = 4
    14+6+4 = 24

    44 - 20 = 24

2
    1:  2-1 = 1 * 2 = 2
    2:  2-2 = 0 * 14 = 0
    3:  3-2 = 1 * 3 = 3
    5:  5-2 = 3 * 1 = 3
    2+3+3 = 8

    24 - 


3
    1:  3-1 = 2 * 2 = 4
    2:  3-2 = 1 * 14 = 14
    3:  3-3 = 0 * 3 = 0
    5:  5-3 = 2 * 1 = 2
    4+14+0+2 = 20

5
    1:  5-1 = 4 * 2 = 8
    2:  5-2 = 3 * 14 = 42
    3:  5-3 = 2 * 3 = 6
    5:  5-5 = 0 * 1 = 0
    8+42+6+0 = 56












    '''