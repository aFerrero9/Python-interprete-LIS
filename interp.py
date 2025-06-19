# Intérprete de LIS+fallas+I/O en Python

# Omega
class Omega:
    def __init__(self, status, state: State, out, inp):
        self.status = status  # "normal" o "abort"
        self.state = state
        self.out = out        # lista acumulada
        self.inp = inp        # resto de la lista de input

# Estado: mapeo de variables a enteros
