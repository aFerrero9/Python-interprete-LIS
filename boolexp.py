# Sintaxis y semántica de expresiones booleanas en LIS
from datatypes import State
from intexp import IntExp
from abc import ABC, abstractmethod

class BoolExp(ABC):
    @abstractmethod
    def run(self, state: State) -> bool:
        pass

class TrueConst(BoolExp):
    def run(self, state):
        return True

class FalseConst(BoolExp):
    def run(self, state):
        return False

class Eq(BoolExp):
    def __init__(self, left: IntExp, right: IntExp):
        self.left, self.right = left, right
    def run(self, state):
        return self.left.run(state) == self.right.run(state)

class Lt(BoolExp):
    def __init__(self, left: IntExp, right: IntExp):
        self.left, self.right = left, right
    def run(self, state):
        return self.left.run(state) < self.right.run(state)
    
class Le(BoolExp):
    def __init__(self, left: IntExp, right: IntExp):
        self.left, self.right = left, right
    def run(self, state):
        return self.left.run(state) <= self.right.run(state)
    
class Gt(BoolExp):
    def __init__(self, left: IntExp, right: IntExp):
        self.left, self.right = left, right
    def run(self, state):
        return self.left.run(state) > self.right.run(state)
    
class Ge(BoolExp):
    def __init__(self, left: IntExp, right: IntExp):
        self.left, self.right = left, right
    def run(self, state):
        return self.left.run(state) >= self.right.run(state)

class Not(BoolExp):
    def __init__(self, p: BoolExp):
        self.p = p
    def run(self, state):
        return not self.p.run(state)

class And(BoolExp):
    def __init__(self, p: BoolExp, q: BoolExp):
        self.p, self.q = p, q
    def run(self, state):
        return self.p.run(state) and self.q.run(state)

class Or(BoolExp):
    def __init__(self, p: BoolExp, q: BoolExp):
        self.p, self.q = p, q
    def run(self, state):
        return self.p.run(state) or self.q.run(state)
