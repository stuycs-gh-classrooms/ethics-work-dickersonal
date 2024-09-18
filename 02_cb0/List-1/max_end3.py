def max_end3(nums):
  big = 0;
  if nums[0] > nums[-1]:
    big = nums[0]
  else:
    big = nums[-1]
  for i in range(len(nums)):
    nums[i] = big
  return nums
