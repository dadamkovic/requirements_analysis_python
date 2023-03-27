from abc import ABC, abstractmethod, abstractproperty
from ExceptionsDefs import *




class SigType(ABC):
  def __init__(self):
    self.__sig_type = None

  @abstractproperty
  def sig_type(self):
    return self.__sig_type

class Enum(SigType):

  @classmethod
  def __checkValidInit(enum_vals):
    if len(enum_vals) > 1:
         raise TooFewValuesEnum("Provide More values")
    val_t = type(enum_vals[0])
    if not all(type(item)==val_t for item in enum_vals):
      raise DifferentTypesEnum("Items in ENUM don't have the same type")
    return True

  def __init__(self, enum_vals):
    self.super().__init__()
    self.__checkValidInit(enum_vals)
    self.__vals = enum_vals
 
  @property
  def vals_type(self):
    return type(self.__vals[0])

  @property
  def vals(self):
    return self.__vals