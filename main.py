from datatypes import Omega, State
from comm import Assign, Output, Seq, Input, Skip, Fail, While, NewVar, Catchin
from boolexp import Lt
from intexp import Num, Var, Plus

# Archivo para probar programas a mano. Simplemente cambiar prog
"""
LIS pseudocódigo:
x := 0 ;
while x < 5 do (
  ?y ;
  !y ;
  x := x + 1
)  
""" 
# Construcción del AST
prog = Seq(
    Assign("x", Num(0)),
    While(
        Lt(Var("x"), Num(5)),
        Seq(
            Input("y"),
            Seq(
                Output(Var("y")),
                Assign("x", Plus(Var("x"), Num(1)))
            )
        )
    )
)
# Estado y salida iniciales
st0 = State()    # {}
out0 = []        # []

omega = prog.run(st0, out0)

print("Status:", omega.status)   
print("State: ", omega.state)    
print("Output:", omega.out)
