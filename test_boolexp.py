import unittest
from datatypes import State
from intexp import Num, Var
from boolexp import (
    TrueConst, FalseConst, Eq, Lt, Le, Gt, Ge, Not, And, Or
)

class TestBoolExp(unittest.TestCase):
    def setUp(self):
        self.state = State()
        # inicializamos algunas variables para los tests
        self.state['a'] = 5
        self.state['b'] = 3

    def test_true_false(self):
        self.assertTrue(TrueConst().run(self.state))
        self.assertFalse(FalseConst().run(self.state))

    def test_eq(self):
        self.assertTrue(Eq(Num(4), Num(4)).run(self.state))
        self.assertFalse(Eq(Num(4), Num(5)).run(self.state))
        # con variables
        self.assertTrue(Eq(Var('a'), Num(5)).run(self.state))
        self.assertFalse(Eq(Var('b'), Num(5)).run(self.state))

    def test_lt(self):
        self.assertTrue(Lt(Num(2), Num(3)).run(self.state))
        self.assertFalse(Lt(Num(3), Num(2)).run(self.state))

    def test_le(self):
        self.assertTrue(Le(Num(3), Num(3)).run(self.state))
        self.assertTrue(Le(Num(2), Num(5)).run(self.state))
        self.assertFalse(Le(Num(5), Num(2)).run(self.state))

    def test_gt(self):
        self.assertTrue(Gt(Num(5), Num(2)).run(self.state))
        self.assertFalse(Gt(Num(2), Num(5)).run(self.state))

    def test_ge(self):
        self.assertTrue(Ge(Num(5), Num(5)).run(self.state))
        self.assertTrue(Ge(Num(6), Num(5)).run(self.state))
        self.assertFalse(Ge(Num(2), Num(5)).run(self.state))

    def test_not(self):
        self.assertTrue(Not(FalseConst()).run(self.state))
        self.assertFalse(Not(TrueConst()).run(self.state))

    def test_and(self):
        self.assertTrue(And(TrueConst(), TrueConst()).run(self.state))
        self.assertFalse(And(TrueConst(), FalseConst()).run(self.state))
        self.assertFalse(And(FalseConst(), TrueConst()).run(self.state))

    def test_or(self):
        self.assertTrue(Or(TrueConst(), FalseConst()).run(self.state))
        self.assertTrue(Or(FalseConst(), TrueConst()).run(self.state))
        self.assertFalse(Or(FalseConst(), FalseConst()).run(self.state))

if __name__ == '__main__':
    unittest.main()
