from abc import ABC, abstractmethod
from ExceptionsDefs import *


def getId():
  requirement_id = 0
  while(True):  
    yield requirement_id
    requirement_id += 1

id_generator = getId()

class RequirementClass(ABC):
  __lastID = 0

  @abstractmethod
  def addCondition(self, condition):
    pass

class FunctionalRequirement(RequirementClass):
  
  def __init__(self, name):
    self.name = name
    self.__conditions = []
    self.__actions = []
    #todo: clean up this it doesn't look good
    self.__req_id = next(id_generator)

  def addCondition(self, condition):
    try: 
      condition()
    except Exception:
      raise ConditionFaultErr("The supplied condition is not valid!")
    
    self.__conditions.append(condition)
  
  def addAction(self, action):
    #todo: implement some check if the action is valid wihtout running it
    self.__actions.append(action)

  def evaluateConditions(self):
    res = True
    for cond in self.__conditions:
      res = res and cond()
    
    return res
  
  def runActions(self):
    for action in self.__actions:
      action()
  
  def runRequirement(self):
    if self.evaluateConditions() is True:
      self.runActions()
      return True
    else:
      return False

  