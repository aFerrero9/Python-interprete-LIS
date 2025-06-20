from datatypes import Omega, State
from comm import Assign
from intexp import Num

# Construcción del AST
prog = Assign("x", Num(5))

# Estado y salida iniciales
st0 = State()    # {}
out0 = []        # []

# Ejecutamos
omega = prog.run(st0, out0)

print("Status:", omega.status)   # debería ser "normal"
print("State: ", omega.state)    # {'x': 5}
print("Output:", omega.out)      # []
