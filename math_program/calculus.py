"""
Calculus Module
Contains calculus operations including derivatives, integrals, and limits.
"""
import numpy as np
from typing import Callable, Union, List
from scipy import integrate

class Calculus:
    @staticmethod
    def derivative(f: Callable[[float], float], x: float, h: float = 1e-7) -> float:
        """
        Calculate numerical derivative of function f at point x using central difference method
        Args:
            f: Function to differentiate
            x: Point at which to calculate derivative
            h: Small step size
        Returns:
            Derivative value
        """
        return (f(x + h) - f(x - h)) / (2 * h)

    @staticmethod
    def partial_derivative(f: Callable[[List[float]], float], x: List[float], 
                         variable: int, h: float = 1e-7) -> float:
        """
        Calculate partial derivative with respect to one variable
        Args:
            f: Multivariable function to differentiate
            x: Point at which to calculate derivative [x1, x2, ...]
            variable: Index of variable to differentiate with respect to
            h: Small step size
        Returns:
            Partial derivative value
        """
        x_plus = x.copy()
        x_minus = x.copy()
        x_plus[variable] += h
        x_minus[variable] -= h
        return (f(x_plus) - f(x_minus)) / (2 * h)

    @staticmethod
    def definite_integral(f: Callable[[float], float], a: float, b: float, 
                         method: str = 'trapezoid', n: int = 1000) -> float:
        """
        Calculate definite integral using various methods
        Args:
            f: Function to integrate
            a: Lower bound
            b: Upper bound
            method: Integration method ('trapezoid', 'simpson', or 'quad')
            n: Number of intervals (for trapezoid and simpson methods)
        Returns:
            Integral value
        """
        if method == 'trapezoid':
            x = np.linspace(a, b, n)
            y = np.array([f(xi) for xi in x])
            return np.trapz(y, x)
        elif method == 'simpson':
            return integrate.simps([f(x) for x in np.linspace(a, b, n)], np.linspace(a, b, n))
        elif method == 'quad':
            result, _ = integrate.quad(f, a, b)
            return result
        else:
            raise ValueError("Invalid method. Choose 'trapezoid', 'simpson', or 'quad'")

    @staticmethod
    def limit(f: Callable[[float], float], x: float, side: str = 'both', h: float = 1e-7) -> float:
        """
        Calculate limit of function f as x approaches a point
        Args:
            f: Function to evaluate limit
            x: Point to approach
            side: 'left', 'right', or 'both'
            h: Small step size
        Returns:
            Limit value
        Raises:
            ValueError: If left and right limits don't match for side='both'
        """
        if side == 'left':
            return f(x - h)
        elif side == 'right':
            return f(x + h)
        else:
            left_limit = f(x - h)
            right_limit = f(x + h)
            if abs(left_limit - right_limit) < h:
                return (left_limit + right_limit) / 2
            raise ValueError("Left and right limits do not match")

    @staticmethod
    def taylor_series(f: Callable[[float], float], x: float, a: float, 
                     n: int = 4) -> Callable[[float], float]:
        """
        Generate Taylor series approximation of function f around point a
        Args:
            f: Function to approximate
            x: Variable of the resulting polynomial
            a: Point around which to expand
            n: Number of terms (degree + 1)
        Returns:
            Function representing Taylor polynomial
        """
        def factorial(k):
            if k == 0:
                return 1
            return k * factorial(k - 1)

        def taylor_term(k):
            if k == 0:
                return f(a)
            h = 1e-7
            derivative = Calculus.derivative(
                lambda t: taylor_term(k-1), 
                a, 
                h
            )
            return derivative * (x - a)**k / factorial(k)

        return sum(taylor_term(i) for i in range(n))
