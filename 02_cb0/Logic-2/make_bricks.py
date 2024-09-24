def make_bricks(small, big, goal):
  while goal >= 5 and big > 0:
    goal = goal - 5
    big = big - 1
  while goal >= 1 and small > 0:
    goal = goal - 1
    small = small - 1
  return goal == 0