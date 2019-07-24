def threeSumClosest(nums: list, target: int) -> int:
    nums.sort()
    sprev = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums)
        sum = 


nums = [-1, 2, 1, -4]
target = 1


threeSumClosest(nums, target)
