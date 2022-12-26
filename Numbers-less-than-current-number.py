class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        _list = []
        for num in nums:
            count = 0

            for num2 in nums:
                if num2 < num:
                    count += 1

            _list.append(count)

        return _list
