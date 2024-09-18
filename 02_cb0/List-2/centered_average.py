def centered_average(nums):
  small = 0
  big = 0
  sums = 0
  for i in range(len(nums)):
    if nums[small] > nums[i]:
      small = i
    if nums[big] < nums[i]:
      big = i
  for i in range(len(nums)):
    if (not(nums[i] == nums[big]) and not(nums[i] == nums[small])):
      sums += nums[i]
  return sums/(len(nums)-2)
