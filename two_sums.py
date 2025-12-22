class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for k,v in enumerate(nums):
            need = target - v
            if need in map:
                return [map[need], k]
            map[v] = k
