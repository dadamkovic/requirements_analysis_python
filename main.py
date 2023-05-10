from MiscClasses import *
from Requirement import FuncReq
from Conditions import *
from Actions import *
from SignalClassDefs import *

if __name__ == "__main__":

    parameter = Parameter("Some Param", 2)
    timer = Timer("Timer A", 8, 0.1)

    some_signal_A = SignalEnum("Signal A", [1, 2, 3])
    some_signal_B = SignalEnum("Signal B", [1, 2, 3])
    some_signal_C = SignalEnum("Signal C", [1, 4, 2, 3])

    cond1 = some_signal_A > parameter
    cond2 = some_signal_A > parameter

    cond3 = ConditionGroup()
    cond3.cond = [cond1, 'AND', cond2]

    req0 = FuncReq("Some Requirement")
    req0.conditions = [
        cond1,
        "AND",
        cond2,
        "OR",
        cond3]

    action1 = Set(some_signal_A, 3)
    action2 = Set(some_signal_A, 1)
    action3 = Start(timer)
    action4 = Stop(timer)
    action5 = Reset(timer)
    
    req0.actions = [action1, action2, action3]

    print(req0.value)

    some_signal_A.checkIntegrity()
    timer.checkIntegrity()
