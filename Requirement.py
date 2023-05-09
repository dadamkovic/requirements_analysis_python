from ExceptionsDefs import *
from MiscClasses import Comparison, Condition, ConditionGroup



class ReqType():
    pass

class FuncReq(ReqType):
  def __init__(self,  name):
    self.name = name

    self._conditions = ConditionGroup()

  @property
  def conditions(self):
    return self._conditions.value[1:-1]
     
  @conditions.setter
  def conditions(self, lst):   
    self._conditions.cond = lst


    
        