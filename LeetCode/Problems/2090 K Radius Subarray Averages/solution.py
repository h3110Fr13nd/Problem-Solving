from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if len(nums) <= 2*k:
            return [-1]*len(nums)
        queue = [-1]*k
        len_nums = len(nums)
        sum = 0
        for i in range(len_nums):
            sum+=nums[i]
            if i>=2*k:
                queue.append(int(sum/(2*k+1)))

                sum-=nums[i-2*k]
        queue += [-1]*k
        return queue


def test():
    solution = Solution()
    assert solution.getAverages([7,4,3,9,1,8,5,2,6],3) == [-1,-1,-1,5,4,4,-1,-1,-1] , "Failed"
    assert solution.getAverages([100000],0) == [100000] , "Failed"
    assert solution.getAverages([8],100000) == [-1] , "Failed"

if __name__ == "__main__":
    test()
    print("Passed All Testcases")