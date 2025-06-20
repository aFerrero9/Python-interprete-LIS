import unittest
from datatypes import State
from intexp import Num, Var, Neg, Plus, Sub, Mul, Div, Mod

class TestIntExp(unittest.TestCase):
    def setUp(self):
        # Cada test empieza con un estado limpio
        self.state = State()

    def test_num(self):
        self.assertEqual(Num(42).run(self.state), 42)

    def test_var_uninitialized(self):
        # 'x' no está en el estado, debería inicializarse a 0
        self.assertEqual(Var('x').run(self.state), 0)
        self.assertIn('x', self.state)
        self.assertEqual(self.state['x'], 0)

    def test_var_initialized(self):
        self.state['y'] = 5
        self.assertEqual(Var('y').run(self.state), 5)

    def test_neg(self):
        expr = Neg(Num(3))
        self.assertEqual(expr.run(self.state), -3)

    def test_plus(self):
        expr = Plus(Num(2), Num(3))
        self.assertEqual(expr.run(self.state), 5)

    def test_sub(self):
        expr = Sub(Num(5), Num(2))
        self.assertEqual(expr.run(self.state), 3)

    def test_mul(self):
        expr = Mul(Num(4), Num(3))
        self.assertEqual(expr.run(self.state), 12)

    def test_div(self):
        expr = Div(Num(7), Num(2))
        self.assertEqual(expr.run(self.state), 3) 

    def test_mod(self):
        expr = Mod(Num(7), Num(2))
        self.assertEqual(expr.run(self.state), 1)

if __name__ == '__main__':
    unittest.main()
