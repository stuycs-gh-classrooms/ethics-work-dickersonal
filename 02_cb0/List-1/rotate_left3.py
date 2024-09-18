def rotate_left3(nums):
  temp = 0
  for i in range(len(nums)-1):
    if i == 0:
      temp = nums[i]
    nums[i] = nums[i+1]
  nums[-1] = temp
  return nums
