from ExceptionsDefs import ImpossibleValue
import numbers

class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = type(value)
    
    def set(self, val):
        if type(val) == self.type:
            return True
        raise ImpossibleValue("Expected {} ; Recieved {}".format(self.type, type(val)))
    
class Timer:
    def __init__(self, name, maximum, resolution):
        if not isinstance(maximum, numbers.Real) or \
        not isinstance(resolution, numbers.Real) or \
        maximum < resolution:
            raise ImpossibleValue("Values were max: {}; res: {}".format(maximum, resolution))
        
        self.name = name
        self.maximum = maximum
        self.resolution = resolution
        self.__has_starter = False
        self.__has_stopper = False
        self.__has_reseter = False
    
    def start(self):
        self.__has_starter = True
        return True
    
    def stop(self):
        self.__has_stopper = True
        return True
    
    def reset(self):
        self.__has_reseter = True
        return True
    
    def checkIntegrity(self):
        if not self.__has_starter:
            print("Warning: Timer '{}' is never started!".format(self.name))
        if not self.__has_stopper:
            print("Warning: Timer '{}' is never stopped!".format(self.name))
        if not self.__has_reseter:
            print("Warning: Timer '{}' is never reseted!".format(self.name))
