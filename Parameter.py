class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.type = type(value)