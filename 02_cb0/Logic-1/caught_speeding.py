def caught_speeding(speed, is_birthday):
  result = 0
  bdayBonus = 0
  if is_birthday:
    bdayBonus = 5
  if speed <= 61+bdayBonus:
    result = 0
  elif speed <= 80+bdayBonus:
    result = 1
  elif speed > 80+bdayBonus:
    result = 2
  return result
