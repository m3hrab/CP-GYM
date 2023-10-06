class Solution:
    def __init__(self, nums) -> int:
        self.nums = nums
    def removeDuplicates(self):
        if not self.nums:
            return 0
        slow = 0
        for fast in range(1,len(self.nums)):
            if self.nums[slow] != self.nums[fast]:
                slow += 1
                self.nums[slow] = self.nums[fast]
        
        return slow + 1
    

nums = [2,7,7,9,9,11]
obj = Solution(nums)

k = obj.removeDuplicates()
print(obj.nums[:k])
print(k)