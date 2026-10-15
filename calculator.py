#!/usr/bin/env python3
"""A simple calculator for arithmetic expressions."""

from __future__ import annotations

import ast
from typing import Union


Number = Union[int, float]


def calculate(expression: str) -> Number:
    """Safely evaluate a basic arithmetic expression."""
    node = ast.parse(expression, mode="eval")
    return _eval(node.body)


def _eval(node: ast.AST) -> Number:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
    if isinstance(node, ast.UnaryOp):
        value = _eval(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +value
        if isinstance(node.op, ast.USub):
            return -value
    raise ValueError("Unsupported expression")


def main() -> None:
    expression = input("Enter expression: ")
    print(calculate(expression))


if __name__ == "__main__":
    main()
