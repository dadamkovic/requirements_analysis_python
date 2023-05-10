from ExceptionsDefs import *
from Conditions import *
from Actions import *



class ReqType():
    pass

class FuncReq(ReqType):
  def __init__(self,  name):
    self.name = name

    self.__conditions = ConditionGroup()
    self.__actions = None

  @property
  def conditions(self):
    return self.__conditions.value[2:-2]
     
  @conditions.setter
  def conditions(self, lst):   
    self.__conditions.cond = lst


  @property
  def actions(self):
    text = ""
    for act in self.__actions:
      text += act.value + '\n'
    return text
  
  @actions.setter
  def actions(self, actions):
    self.__actions = ActionGroup(actions)

  @property
  def value(self):
    text = "{}:\n".format(self.name)
    text += "IF\n{}\nTHEN\n{}".format(self.conditions, self.actions)
    return text


    
        