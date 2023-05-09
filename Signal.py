"""

"""

from ExceptionsDefs import *
from SignalClassDefs import *
from MiscClasses import *


class Signal:

        

    def __init__(self, sig_name, sig_class):
      if not issubclass(type(sig_class), SigType):
        raise WrongClassSignal("Signal class has to be of sub-class SigType")
      
      self.name = sig_name
      self.type = sig_class.type
      self.cls = sig_class

    def __eq__(self, other):
      self.checkTypeMatch(other)
      return Comparison(self, other, "==")
    def __lt__(self, other):
      self.checkTypeMatch(other)
      return Comparison(self, other, "<")
    def __gt__(self, other):
      self.checkTypeMatch(other)
      return Comparison(self, other, ">")
    def __rshift__(self, other):
      self.checkTypeMatch(other)
      return Comparison(self, other, "CHANGES TO")
    