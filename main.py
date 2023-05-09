from Signal import *
from Parameter import *
from Requirement import FuncReq

if __name__ == "__main__":

  LIN_signals = SignalEnum([1,2,3])
  HW_signals = SignalEnum([3,4])

  parameter = Parameter("Some Param", 2)

  some_signal_A = Signal("Signal A", LIN_signals)
  some_signal_B = Signal("Signal B", LIN_signals)
  some_signal_C = Signal("Signal B", HW_signals)

  cond1 = some_signal_A > parameter
  cond2 = some_signal_A > parameter

  cond3 = ConditionGroup()
  cond3.cond = [cond1,'AND',cond2]

  req0 = FuncReq("Some Requirement")
  req0.conditions = [
    cond1, 
    "AND", 
    cond2,
    "OR",
    cond3]
  
print(req0.conditions)

