

"""
box is a list of strings and boxSearch will see if "box" 
is inside the list (return true) or not (return false)
"""
def boxSearch(box):
  numItems = len(box)
  if (numItems == 0):
    return(False)
  
  item = box[-1] #gets the last item in list
  if (item == "star"): #sees if the item is a star
    return(True)
  else:
    #this removes the last item from the box and searches the rest
    restOfBox = box[:-1]
    return boxSearch(restOfBox)

box = ["truffle","star","pencil","chocolate","bottle"]
print(boxSearch(box))
