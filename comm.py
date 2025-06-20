# comm.py
from abc import ABC, abstractmethod
from datatypes import State, Omega
from intexp import IntExp
from boolexp import BoolExp

class Comm(ABC):
    """
    Las funciones devolverán un estado nuevo, no actualizarán el estado de entrada.
    De esta forma aseguramos un estilo "funcional" fiel a la teoría  
    """ 
    @abstractmethod
    def run(self, state: State, out: list[int]) -> Omega:
        # Ejecuta el comando en (state, out) y devuelve el nuevo Omega
        pass

class Skip(Comm):
    def run(self, state, out):
        new_state = State(state)
        return Omega("normal", new_state, out)
    
class Fail(Comm):
    def run(self, state, out):
        new_state = State(state)
        return Omega("abort", new_state, out)
    
class Assign(Comm):
    def __init__(self, var: str, expr: IntExp):
        self.var, self.expr = var, expr

    def run(self, state: State, out: list[int]):
        val = self.expr.run(state)
        new_state = State(state)
        new_state[self.var] = val
        return Omega("normal", new_state, out) 

class Output(Comm):
    def __init__(self, expr: IntExp):
        self.expr = expr

    def run(self, state, out):
        val = self.expr.run(state)
        new_state = State(state)
        new_out = out + [val]
        return Omega("normal", new_state, new_out)

class If(Comm):
    def __init__(self, cond: BoolExp, c0: Comm, c1: Comm):
        self.cond, self.c0, self.c1 = cond, c0, c1

    def run(self, state, out):
        if self.cond.run(state):
            return self.c0.run(state, out)
        else:
            return self.c1.run(state, out)
        
class Input(Comm):
    def __init__(self, var: str):
        self.var = str(var)

    def run(self, state, out):
        # Pedimos un entero al usuario
        while True:
            try:
                s = input(f"Ingrese un valor entero para '{self.var}': ")
                user_input = int(s)
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
        
        # Copia funcional del estado
        new_state = State(state)
        new_state[self.var] = user_input
        
        # Como sólo usos un input a la vez, la cola queda vacía
        return Omega("normal", new_state, out)

def estrella(om: Omega, comm: Comm) -> Omega:
    # Función de transferencia de control. Propagación de error
    if om.status == "abort":
        return om
    return comm.run(om.state, om.out)

class Seq(Comm):
    def __init__(self, c0: Comm, c1: Comm):
        self.c0, self.c1 = c0, c1

    def run(self, state, out):
        return estrella(self.c0.run(state, out), self.c1)
    
def cruz(om: Omega, comm: Comm) -> Omega:
    # Función de transferencia de control para catchin. Dual de estrella
    if om.status == "normal":
        return om
    return comm.run(om.state, om.out)

class Catchin(Comm):
    def __init__(self, c0: Comm, c1: Comm):
        self.c0, self.c1 = c0, c1

    def run(self, state, out):
        return cruz(self.c0.run(state, out), self.c1)

class While(Comm):
    def __init__(self, cond: BoolExp, body: Comm):
        self.cond, self.body = cond, body

    def run(self, state, out):
        om = Omega("normal", State(state), out)

        # mientras cond = true, encadeno body con estrella
        while self.cond.run(om.state):
            om = estrella(om, self.body)
            # si el estado es abort, salimos del bucle
            # con esto me aseguro que el programa while True do fail termine
            if om.status == "abort":
                return om

        return om
    
class NewVar(Comm):
    def __init__(self, var: str, expr: IntExp, c: Comm):
        self.var, self.expr, self.c = var, expr, c

    def run(self, state, out):
        temp_state = State(state)
        # guardo valor original de la variable
        old = temp_state.get(self.var, None)
        # inicializo la variable en la copia
        temp_state[self.var] = self.expr.run(state)

        om = self.c.run(temp_state, out)
        # 
        restored = State(om.state)
        if old is None:
            # si no existía antes, la elimino del estado
            restored.pop(self.var, None)
        else:
            restored[self.var] = old

        return Omega(om.status, restored, om.out)

