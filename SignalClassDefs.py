from abc import ABC, abstractmethod, abstractproperty
from ExceptionsDefs import *




class SigType(ABC):
  def __init__(self):
    self.type = None
  
  @abstractmethod
  def checkValidInit(self):
    pass


  @abstractmethod
  def checkComparison(self):
    pass

class SignalEnum(SigType):

  def checkValidInit(self, enum_vals):
    if len(enum_vals) == 1:
         raise TooFewValuesEnum("Provide More values")
    self.type = type(enum_vals[0])
    if not all(type(item)==self.type for item in enum_vals):
      raise DifferentTypesEnum("Items in ENUM don't have the same type")
    return True
  
  def checkComparison(self, other):
    if other.value not in self.__vals:
      raise ImpossibleValueSignal("Signal cannot assume this value!")
    return True

  def __init__(self, enum_vals):
    super().__init__()
    self.checkValidInit(enum_vals)
    self.__vals = enum_vals



 