nums = [5, 5, 5] 
nums = sorted(list(set(nums)))
if len(nums)>1: print(nums[1])
else: print('Второго по величине элемента нет')
