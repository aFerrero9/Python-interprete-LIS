# Intérprete de LIS+fallas+I/O en Python
"""
Interpretación Omega:
Es una abstracción del omega real. 
- status indica si tenemos algo de iota_term(normal),
o algo de iota_abort(abort).
- no tenemos iota_out, la abstracción se hace definiendo
la lista que representan los valores impresos(out).
- iota_in no existe, simplemente le pedimos el input al usuario en el momento.
"""
# Estado: mapeo de variables a enteros
class State(dict):
    def __init__(self, state: dict = {}):
        super().__init__(state)

# Omega
class Omega:
    def __init__(self, status, state: State, out: list[int]):
        self.status = status  # "normal" o "abort"
        self.state = state    # estado actual
        self.out = out        # lista acumulada
    # EXTENDER CON F DE TRANSFERENCIA DE CONTROL

