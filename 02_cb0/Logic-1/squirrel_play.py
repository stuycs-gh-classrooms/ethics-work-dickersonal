def squirrel_play(temp, is_summer):
  upperTemp = 90
  if is_summer:
    upperTemp = 100
  return (temp >= 60 and temp <= upperTemp)
    
