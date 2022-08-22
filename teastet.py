import re

def removeMultiSpace(str):
  str = re.sub(r"[?|$|'|!|`|\"]",r'',str)
  return " ".join(str.split())

print(removeMultiSpace("this is my 'string "))
