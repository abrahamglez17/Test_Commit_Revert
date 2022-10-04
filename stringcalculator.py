


def Add(a):
  #Add implementation

  # simplest case
  if(a == ""):
    return 0
  
  elif(a.isdigit() and len(a) == 1):
    return int(a)