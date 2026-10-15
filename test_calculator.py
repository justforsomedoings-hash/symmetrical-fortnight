import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_operator_precedence(self) -> None:
        self.assertEqual(calculate("1 + 2 * 3"), 7)

    def test_parentheses(self) -> None:
        self.assertEqual(calculate("(1 + 2) * 3"), 9)

    def test_unary(self) -> None:
        self.assertEqual(calculate("-5 + 2"), -3)

    def test_invalid_expression(self) -> None:
        with self.assertRaises(ValueError):
            calculate("__import__('os').system('echo bad')")


if __name__ == "__main__":
    unittest.main()
