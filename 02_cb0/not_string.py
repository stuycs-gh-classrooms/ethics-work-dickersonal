def not_string(str):
  if(str>=3):
    if(str[0:3] == "not"):
      return str
    else:
      return "not " + str

