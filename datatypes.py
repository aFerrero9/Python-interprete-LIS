# Intérprete de LIS+fallas+I/O en Python

# Estado: mapeo de variables a enteros
class State(dict):
    def __init__(self, state: dict = {}):
        super().__init__(state)

# Omega
class Omega:
    def __init__(self, status, state: State, out, inp):
        self.status = status  # "normal" o "abort"
        self.state = state    # estado actual
        self.out = out        # lista acumulada
        self.inp = inp        # resto de la lista de input
    # EXTENDER CON F DE TRANSFERENCIA DE CONTROL

