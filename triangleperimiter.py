nums=[2,1,2]
def largestPerimeter(nums):
    nums.sort()
    print(range(len(nums)-3, -1, -1))
    for i in range(len(nums)-3, -1, -1):
        if nums[i] + nums[i+1] > nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0
print(largestPerimeter(nums))
