class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        indexList = []

        for i,num in enumerate(nums):

            if num == target:

                indexList.append(i)

        return indexList
