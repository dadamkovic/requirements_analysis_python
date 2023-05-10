from abc import ABC, abstractmethod, abstractproperty
from ExceptionsDefs import *
from Conditions import *

class SigType(ABC):
    def __init__(self, name, typ):
        self.type = typ
        self.name = name
        self._setter = []

    @abstractmethod
    def checkValidInit(self):
        pass

    @abstractmethod
    def checkValue(self):
        pass

    def checkTypeMatch(self, other):
        if (hasattr(other, "name")) and (hasattr(other, "value")):
            return self.checkValue(other.value)

        raise WrongRelationError("Inputs not compatible!")

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


class SignalEnum(SigType):
    def __init__(self, name, enum_vals): 
        self.checkValidInit(enum_vals)

        super().__init__(name, type(enum_vals[0]))
        self.__vals = enum_vals
        
    def checkValidInit(self, enum_vals):
        if len(enum_vals) == 1:
            raise TooFewValuesEnum("Provide More values")
        
        self.type = type(enum_vals[0])
        if not all(type(item) == self.type for item in enum_vals):
            raise DifferentTypesEnum("Items in ENUM don't have the same type")
        
        if len(set(enum_vals)) != len(enum_vals):
            raise InitRepeatingValuesEnum("Repeating entries in Enum definition.")
        return True

    def checkValue(self, value):
        if value not in self.__vals:
            raise ImpossibleValueSignal("Signal cannot assume this value!")
        return True
    
    def checkIntegrity(self):
        if self._setter is []:
            print("Warning: Signal '{}' not set".format(self.name))
        
        if len(set(self._setter)) != len(self.__vals):
            print("Warning: Signal '{}' not all values reachable".format(self.name))

    def set(self, value):
        self.checkValue(value)
        self._setter.append(value)



