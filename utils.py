from datatypes import Omega
from comm import Comm

def estrella(om: Omega, comm: Comm) -> Omega:
    # Función de transferencia de control. Propagación de error
    if om.status == "abort":
        return om
    return comm.run(om.state, om.out)

def cruz(om: Omega, comm: Comm) -> Omega:
    # Función de transferencia de control para catchin. Dual de estrella
    if om.status == "normal":
        return om
    return comm.run(om.state, om.out)
