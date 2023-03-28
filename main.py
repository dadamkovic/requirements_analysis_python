from Signal import *
from Requirement import FunctionalRequirement

if __name__ == "__main__":

  numbers = Enum([1,2,3,4,5])

  sig_a = Signal("someSigA", numbers, 2)
  sig_b = Signal("someSigB", numbers, 3)
  sig_c = Signal("someSigC", numbers, 4)

  req0 = FunctionalRequirement("some req")
  req0.addCondition(sig_a < sig_b)
  #req0.addCondition(sig_a < sig_c)
  req0.addAction(lambda:print("A < B"))
  req0.addAction(lambda:print("Hello There"))
  req0.addAction(lambda:setSignal(sig_c, 3))
  req0.runRequirement()
  print(str(sig_c.sig_value))
  print("All OK")
