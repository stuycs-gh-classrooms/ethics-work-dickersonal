def sum13(nums):
  if(len(nums) > 0):
    thirteen = False
    countThirt = 0
    sum = 0
    for i in nums:
      if (not i == 13) or not thirteen:
        sum+=i
        thirteen = False
      else:
        thirteen = True
        countThirt+=1
    return sum/(len(nums)-countThirt)
  else:
    return 0

