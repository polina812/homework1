nums = [1, 2, 3, 4, 5, 6, 4]
nums = list(set(nums))
target = 7
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==target:
            print(f"({nums[i]}, {nums[j]})")
