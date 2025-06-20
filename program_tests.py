import unittest
from unittest.mock import patch
from datatypes import State
from comm import (
    Seq, Assign, Output, Fail, Skip,
    If, While, NewVar, Input, Catchin
)
from intexp import Num, Var, Plus
from boolexp import Lt

class TestPrograms(unittest.TestCase):
    def test_assign_and_output(self):
        # LIS pseudocódigo: x := 5; !x
        prog = Seq(
            Assign("x", Num(5)),
            Output(Var("x"))
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "normal")
        self.assertEqual(omega.state, {"x": 5})
        self.assertEqual(omega.out, [5])

    def test_fail_sequence(self):
        # LIS pseudocódigo: fail; x := 5
        prog = Seq(
            Fail(),
            Assign("x", Num(5))
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "abort")
        # state should reflect fail's copy but no x assignment
        self.assertNotIn("x", omega.state)
        self.assertEqual(omega.out, [])

    def test_catchin(self):
        # LIS pseudocódigo: ((catchin fail with x := 2); !x) ; z := 10 
        prog = Seq(
            Seq(
                Catchin(Fail(), Assign("x", Num(2))),
                Output(Var("x"))
            ),
            Assign("z", Num(10))  # to test something after catchin
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "normal")
        self.assertEqual(omega.state, {"x": 2, "z": 10})
        self.assertEqual(omega.out, [2])

    def test_if(self):
        # LIS pseudocódigo: if 1 < 2 then x := 1 else x := 2
        prog = If(
            Lt(Num(1), Num(2)),
            Assign("x", Num(1)),
            Assign("x", Num(2))
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "normal")
        self.assertEqual(omega.state, {"x": 1})
        self.assertEqual(omega.out, [])

    def test_print_each_iteration(self):
        # LIS pseudocódigo: x := 0; while x < 3 do (x := x + 1; !x)
        prog = Seq(
            Assign("x", Num(0)),
            While(
                Lt(Var("x"), Num(3)),
                Seq(
                    Assign("x", Plus(Var("x"), Num(1))),
                    Output(Var("x"))
                )
            )
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "normal")
        self.assertEqual(omega.state, {"x": 3})
        self.assertEqual(omega.out, [1, 2, 3])

    def test_newvar_scoping(self):
        # LIS pseudocódigo: (x := 1; newvar x := 5 in [(x := x + 1) ; !x ]) ; !x
        prog = Seq(
            Seq(
                Assign("x", Num(1)),
                NewVar("x", Num(5), Seq(Assign("x", Plus(Var("x"), Num(1))),Output(Var("x"))))
            ),
            Output(Var("x"))
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "normal")
        # outer x remains 1
        self.assertEqual(omega.state, {"x": 1})
        self.assertEqual(omega.out, [6,1])

    @patch('builtins.input', side_effect=['7', '9'])
    def test_input_and_output(self, mock_input):
        # LIS pseudocódigo: ?x; ?y; !x; !y
        prog = Seq(
            Seq(
                Input("x"),
                Input("y")
            ),
            Seq(
                Output(Var("x")),
                Output(Var("y"))
            )
        )
        omega = prog.run(State(), [])
        self.assertEqual(omega.status, "normal")
        self.assertEqual(omega.state, {"x": 7, "y": 9})
        self.assertEqual(omega.out, [7, 9])

if __name__ == '__main__':
    unittest.main()
