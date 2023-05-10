from abc import abstractmethod, ABC
from ExceptionsDefs import WrongAction

class ActionType(ABC):
    def __init__(self, obj, val=None):
        self.obj = obj
        self.val = val
    
    @abstractmethod
    def value(self):
        raise NotImplementedError

class Set(ActionType):
    def __init__(self, obj, val):
        super().__init__(obj, val)
        
        obj.set(val)
    
    @property
    def value(self):
        return "SET '{}' {}".format(self.obj.name, str(self.val))

class Inc(ActionType):
    def __init__(self, obj, val):
        super().__init__(obj, val)
        obj.inc(val)

    @property
    def value(self):
        return "INC '{}' BY ".format(self.obj.name, self.val)

class Start(ActionType):
    def __init__(self, obj):
        super().__init__(obj)
        obj.start()
    
    @property
    def value(self):
        return "START '{}'".format(self.obj.name)

class Stop(ActionType):
    def __init__(self, obj):
        super().__init__(obj)
        obj.stop()
    
    @property
    def value(self):
        return "STOP '{}'".format(self.obj.name)

class Reset(ActionType):
    def __init__(self, obj):
        super().__init__(obj)
        obj.reset()
    
    @property
    def value(self):
        return "RESET '{}'".format(self.obj.name)


class ActionGroup:
    def __init__(self, acts):
        for act in acts:
            if not issubclass(type(act), ActionType):
                raise WrongAction("Action supplied not class ActionType!")
        self.actions = acts

    def __iter__(self):
        return iter(self.actions)
