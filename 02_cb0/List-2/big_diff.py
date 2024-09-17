def big_diff(nums):
  small = 100000
  big = 0
  for i in nums:
    small = min(small, i)
    big = max(big, i)
  return big-small