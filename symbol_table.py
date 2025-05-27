class SymbolTable:
    def __init__(self):
        self.table = {}

    def set(self, name, value):
        self.table[name] = value

    def get(self, name):
        if name not in self.table:
            raise NameError(f"Variable '{name}' not defined")
        return self.table[name]
