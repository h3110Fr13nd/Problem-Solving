
classSolution:

    deftwoSum(self, nums: List[int], target: int) -> List[int]:

    numMaps=dict()

    for i inrange(len(nums)):

    compliment = target - nums[i]

    if compliment in numMaps:

    return [numMaps[compliment],i]

    numMaps[nums[i]] = i

    deftest(self):

    assertself.twoSum([2,7,11,15],9) == [0,1]

    assertself.twoSum([3,2,4],6) == [1,2]

    assertself.twoSum([3,3], 6) == [0,1]

if__name__ == "__main__":

    solution = Solution()

    solution.test()
