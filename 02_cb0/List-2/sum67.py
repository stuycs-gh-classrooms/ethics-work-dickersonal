def sum67(nums):
  if(len(nums)>0):
    inSixToSeven = False
    sum = 0
    for i in nums:
      if(i == 6):
        inSixToSeven = True
      elif(i == 7 and inSixToSeven):
        inSixToSeven = False
      elif(not inSixToSeven):
        sum+=i
    return sum
  return 0
