"""

"""

from ExceptionsDefs import *
from SignalClassDefs import *


_signal_names = []

class SignalBase():
  def __init__(self):
     pass

  def _checkRelation(self, relation):
      if len(relation) != 3:
        raise WrongRelationDefined("The relation is not valid!")
  
  def _checkValidClass(self, cls):
        if not issubclass(type(cls), SigType):
          raise WrongClassSignal("Signal class has to be of sub-class SigType")
        
  def _checkValidCompare(self, cls):
        if not issubclass(type(cls), SignalBase):
          raise WrongClassSignal("Comparison signal class has to be of sub-class SignalBase")

  def _checkSigVal(self, val, cls):
        if not val in cls.vals:
          raise ImpossibleValueSignal("The value of the signal is not possible")

  def _checkSigName(self, sig_name):
    if type(sig_name) != str:
      raise SignalNameNotChar("The signal name must be string!")
    if sig_name in _signal_names:
      raise SignalInUseError("The selected signal name is already used!")
    _signal_names.append(sig_name)

  def _checkValidMatch(self, other):
    assert self.__sig_class == other.sig_class
    assert self.__value_type == other.value_type


class CompSignal(SignalBase):
   
  def __getText(self, item):
    if type(item) is CompSignal:
       return item.relation
    else:
        return item.name

  def __init__(self, left, right, rel, prev_sigs = []):
    self.__signals = prev_sigs
    if type(left) is not str:
       self.__signals.append(left.name)
       left = left.name
       
    if type(right) is not str:
       self.__signals.append(right.name)
       right = right.name

    self.relation = "(" + " ".join([left, rel, right]) + ")"

  @property
  def signals(self):
     self.__signals = sorted(list(set(self.__signals)))
     return self.__signals

  def __lt__(self, other):
    other_txt = self.__getText(other)
    return CompSignal(self.relation, other_txt, ">", self.signals)
    
  def __and__(self, other):
    other_txt = self.__getText(other)
    return CompSignal(self.relation, other_txt, "&", self.signals)
    
  def __or__(self, other):
    other_txt = self.__getText(other)
    return CompSignal(self.relation, other_txt, "|", self.signals)


# note instead of value it is needed to implement circular buffer in order to be able to check 
# changes in the signal 
class Signal(SignalBase):

    def __init__(self, sig_name, sig_class, sig_val):
      super().__init__()
      #raise exception is sig_class is not correct derived frm SigType class
      self._checkValidClass(sig_class)
      self._checkSigName(sig_name)
      self._checkSigVal(sig_val, sig_class)

      self.__name = sig_name
      self.__sig_class = sig_class

      self.__value = sig_val
      self.__value_type = sig_class.vals_type

    @property
    def name(self):
       return self.__name
    
    @name.setter
    def name(self, val):
       self.__checSigName(val)
       self.__name = val

    @property
    def sig_class(self):
      return self.__sig_class

    @property
    def value(self):
      return self.__value

    @value.setter
    def value(self, val):
      self._checkSigVal(val, self.__sig_class)
      self.__value = val

    @property
    def value_type(self):
      return self.__value_type

    def __lt__(self, other):
      return CompSignal(self, other, "<")
      
    def __gt__(self, other):
      return CompSignal(self, other, ">")
      
    def __and__(self, other):
      return CompSignal(self, other, "&")
    
    def __and__(self, other):
      return CompSignal(self, other, "|")
