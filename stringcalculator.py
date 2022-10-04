
number_list = []

def Add(a):
  #Add implementation

  # simplest case
  if(a == ""):
    return 0
  
  # one number case
  elif(a.isdigit() and len(a) == 1):
    return int(a)

  # two number case
  