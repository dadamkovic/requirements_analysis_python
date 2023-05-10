from ExceptionsDefs import *


class Condition:
    pass


class Comparison(Condition):
    def __init__(self, ls, rs, cond):
        self.ls = ls
        self.rs = rs
        self.cond = cond
        self.value = "{} {} {}".format(ls.name, cond, rs.name)


class ConditionGroup(Condition):
    def __init__(self):
        super().__init__()
        self._cond = None

    @property
    def cond(self):
        return self._cond

    @cond.setter
    def cond(self, lst):
        for idx in range(1, len(lst), 2):
            if lst[idx] not in ["AND", "OR"]:
                raise WrongConditionError("Conditions not in correct form!")
        for idx in range(0, len(lst), 2):
            if not issubclass(type(lst[idx]), Condition):
                raise WrongConditionError("Conditions not in correct form!")

        if lst[-1] in ["AND", "OR"]:
            raise WrongConditionError("Conditions not in correct form!")

        self._cond = lst

    @property
    def value(self):
        text = "(\n"
        for idx in range(len(self._cond)):
            if idx % 2 == 0:
                text += self._cond[idx].value + '\n'
            else:
                text += self._cond[idx] + '\n'
        return text + ')'