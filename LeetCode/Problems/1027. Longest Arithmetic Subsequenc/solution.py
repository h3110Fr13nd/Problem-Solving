from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                if (i, diff) in dp:
                    dp[j, diff] = dp[i, diff] + 1
                else:
                    dp[j, diff] = 2
        return max(dp.values())
                


    
        
def test():
    solution = Solution()
    test_cases = [
        [[3,6,9,12], 4],
        [[9,4,7,2,10], 3 ],
        [[20,1,15,3,10,5,8], 4],
        [[11,11,11,11,11],5],
        [[20,1,15,3,15,10,5,8], 4],
        ]
    for test_case in test_cases:
        print(solution.longestArithSeqLength(test_case[0]), test_case[1])

    for test_case in test_cases:
        assert solution.longestArithSeqLength(test_case[0]) == test_case[1]

if __name__ == "__main__":
    test()
    print("Passed All Testcases")

