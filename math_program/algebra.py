"""
Algebra Module
Contains algebraic operations and equation solving capabilities.
"""
import numpy as np
from typing import List, Tuple, Union

class Algebra:
    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
        """
        Solve quadratic equation ax² + bx + c = 0
        Returns tuple of solutions (x1, x2)
        Raises:
            ValueError: If equation has no real solutions
        """
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("No real solutions exist")
        
        x1 = (-b + np.sqrt(discriminant)) / (2*a)
        x2 = (-b - np.sqrt(discriminant)) / (2*a)
        return x1, x2

    @staticmethod
    def solve_linear_system(coefficients: List[List[float]], constants: List[float]) -> List[float]:
        """
        Solve system of linear equations using numpy
        Args:
            coefficients: Matrix of coefficients
            constants: Vector of constants
        Returns:
            List of solutions
        Raises:
            ValueError: If system has no solution or infinite solutions
        """
        try:
            return list(np.linalg.solve(np.array(coefficients), np.array(constants)))
        except np.linalg.LinAlgError:
            raise ValueError("System has no unique solution")

    @staticmethod
    def polynomial_roots(coefficients: List[float]) -> List[float]:
        """
        Find roots of a polynomial
        Args:
            coefficients: List of coefficients [an, an-1, ..., a1, a0]
        Returns:
            List of roots (may include complex numbers)
        """
        return list(np.roots(coefficients))

    @staticmethod
    def matrix_operations(matrix_a: List[List[float]], matrix_b: List[List[float]], operation: str) -> List[List[float]]:
        """
        Perform matrix operations
        Args:
            matrix_a: First matrix
            matrix_b: Second matrix
            operation: One of 'add', 'subtract', 'multiply'
        Returns:
            Resulting matrix
        Raises:
            ValueError: If matrices have incompatible dimensions
        """
        a = np.array(matrix_a)
        b = np.array(matrix_b)
        
        if operation == 'add':
            if a.shape != b.shape:
                raise ValueError("Matrices must have same dimensions for addition")
            return (a + b).tolist()
        elif operation == 'subtract':
            if a.shape != b.shape:
                raise ValueError("Matrices must have same dimensions for subtraction")
            return (a - b).tolist()
        elif operation == 'multiply':
            if a.shape[1] != b.shape[0]:
                raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
            return np.matmul(a, b).tolist()
        else:
            raise ValueError("Invalid operation. Must be 'add', 'subtract', or 'multiply'")
