def string_splosion(str):
  newstr = ''
  for i in range(len(str)):
    newstr+=str[:i+1]
  return newstr  
  

