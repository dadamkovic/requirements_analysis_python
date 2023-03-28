"""

"""

from ExceptionsDefs import *
from SignalClassDefs import *

  

# note instead of value it is needed to implement circular buffer in order to be able to check 
# changes in the signal 
class Signal():

    def __checkValidMatch(self, other):
      assert self.__sig_class == other.sig_class
      assert self.__value_type == other.value_type

    def __init__(self, sig_name, sig_class, sig_val):
      if not issubclass(type(sig_class), SigType):
        raise WrongClassSignal("Signal class has to be of sub-class SigType")
      
      self.sig_name = sig_name
      self.__sig_class = sig_class
      if not sig_val in sig_class.vals:
        raise ImpossibleValueSignal("The value of the signal is not possible")
      self.__value = sig_val
      self.__value_type = type(sig_val)

    @property
    def sig_class(self):
      return self.__sig_class

    @property
    def sig_value(self):
      return self.__value

    @sig_value.setter
    def sig_value(self, val):
      if not val in self.__sig_class.vals:
        raise ImpossibleValueSignal("The value of the signal is not possible")
      self.__value = val

    @property
    def value_type(self):
      return self.__value_type

    def __lt__(self, other):
      self.__checkValidMatch(other)
      return lambda:self.sig_value < other.sig_value

    def __eq__(self, other):
      self.__checkValidMatch(other)
      return lambda:self.sig_value == other.sig_value
    

def setSignal(signal, value):
  signal.sig_value = value