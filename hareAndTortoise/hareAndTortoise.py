def hasCycle(head, tellWhere=False):
  """
  Returns a boolean indicating the presence of a loop in a queue, using the Hare and Tortoise method.
  
    > head is the Ring object indicating the start of the search for a loop.
    
    > tellWhere is a boolean indicating if the function should return the Ring object starting the loop.
      Format should be (True, Ring) if there's a loop and (False, None) if there's not any.
  """
  if head.pointer == head or head.pointer is None:
      return (False,None) if tellWhere else False
  
  tortoise = head
  hare = head.pointer
  
  while hare.pointer is not None and hare.pointer.pointer is not None:
    if tortoise == hare:
      return (True,hare) if tellWhere else True
    tortoise = tortoise.pointer
    hare = hare.pointer.pointer
  
  return (False,None) if tellWhere else False

class Ring:
    def __init__(self, value, pointer=None) -> None:
        """
        Class constructor. Its instances will have the following variables :
        
          > value (-) : Versatile, could be literally anything.
        
          > pointer (Ring or None) : If there's a pointer, it's another Ring object. If there's no pointer, it's None.
        """
        self.value = value
        self.pointer = pointer
    
    def __str__(self) -> str:
      """
      Special method. Returns the value chain of the queue, starting with the Ring object called.
      If there's a loop in the queue, it reduces the display.
      """
      cycled,cycleStart = hasCycle(self,True)
      cursor = self
      chain = []
      
      if cycled: # Si la chaîne possède un cycle
        cycleStartCount = 0
        while cycleStartCount < 2:
          chain.append(cursor.value)
          cursor = cursor.pointer
          if cursor == cycleStart: cycleStartCount += 1
        chain.append("...")
        return " ".join(chain)
      
      else:
        while cursor.pointer is not None:
          chain.append(cursor.value)
          cursor = cursor.pointer
        chain.append(cursor.value)
        return " ".join(chain)

    def changePointer(self, newPointer) -> None:
        """
        Usual method. Returns None. Changes the Ring's pointer to another Ring object.
        No exceptions if the Ring is already pointing to the newPointer.
        """
        assert isinstance(newPointer,Ring), "The element you want the object to point to isn't a Ring object."
        self.pointer = newPointer

    def delPointer(self) -> None:
      """
      Usual method. Deletes the Ring's pointer (sets it to None) and returns the original pointer.
      If the pointer is already None, the function returns None and does nothing.
      """
      if self.pointer is not None:
        originalPointer = self.pointer
        self.pointer = None
        return originalPointer

if __name__ == "__main__":
  six = Ring("et")
  five = Ring("infinies",six)
  four = Ring("boucles",five)
  three = Ring("des",four)
  two = Ring("toujours",three)
  one = Ring("C'est",two)
  six.changePointer(three)

  # We have a loop that's going like this :
  #            ↗ 4 ↘
  #   1 → 2 → 3     5
  #            ↖ 6 ↙
  # (C'est toujours des boucles infinies et des boucles infinies et...)

  print(one)
  print(f"The queue has a loop: {hasCycle(one)}") # Should be True
  
  # We change the pointer of the sixth Ring to another Ring to exit the loop.
  seven = Ring("c'est tout.")
  six.changePointer(seven)

  # The linked list then resembles to this :
  #            ↗ 4 ↘
  #   1 → 2 → 3     5 → 6 → 7 → None
  # (C'est toujours des boucles infinies et c'est tout.)

  print(one)
  print(f"The queue has a loop: {hasCycle(one)}") # Should be False