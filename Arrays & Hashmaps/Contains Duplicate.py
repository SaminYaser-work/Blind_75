class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mySet = set()

        for n in nums:
            if n in mySet:
                return True
            mySet.add(n)

        return False
