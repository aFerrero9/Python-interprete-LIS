# Sintaxis y semántica de expresiones enteras para LIS
from abc import ABC, abstractmethod
from datatypes import State

class Intexp(ABC):
    # Sintaxis abstracta de expresiones enteras
    @abstractmethod
    def run(self, state: State) -> int:
        pass
    
class Num(Intexp):
    def __init__(self, value: int):
        self.value = value

    def run(self, state: State):
        return self.value

class Var(Intexp):
    def __init__(self, name: str):
        self.name = str(name)
    # Decisión de diseño: si la variable no está definida, 
    # se agrega al estado y se inicializa a 0
    def run(self, state: State):
        if self.name not in state:
            state[self.name] = 0
        return state[self.name]
    
class Neg(Intexp):
    def __init__(self, exp: Intexp):
        self.exp = exp
    def run(self, state: State):
        return -self.exp.run(state)
    
class Plus(Intexp):
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def run(self, state: State):
        return self.e1.run(state) + self.e2.run(state)
    
class Sub(Intexp):
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def run(self, state: State):
        return self.e1.run(state) - self.e2.run(state)
    
class Mul(Intexp):
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def run(self, state: State):
        return self.e1.run(state) * self.e2.run(state)
    
class Div(Intexp):
    # división entera
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def run(self, state: State):
        return self.e1.run(state) // self.e2.run(state)
    
class Mod(Intexp):
    # módulo
    def __init__(self, e1, e2):
        self.e1, self.e2 = e1, e2
    def run(self, state: State):
        return self.e1.run(state) % self.e2.run(state)
