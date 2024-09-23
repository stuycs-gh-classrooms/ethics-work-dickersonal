def date_fashion(you, date):
  num = 1
  if you >= 8 or date >= 8:
    num = 2
  if you <= 2 or date <= 2:
    num = 0
  return num
