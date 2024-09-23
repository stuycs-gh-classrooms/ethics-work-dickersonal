def alarm_clock(day, vacation):
  early = "7:00"
  late = "10:00"
  off = "off"
  if day >= 1 and day <= 5:
    if not vacation:
      return early
    else:
      return late
  elif not vacation:
    return late
  return off