"""
Main Module
Provides a command-line interface for the advanced mathematics program.
"""
from basic_math import BasicMath
from algebra import Algebra
from calculus import Calculus
from statistics import Statistics
import numpy as np
from typing import Callable

class MathProgram:
    @staticmethod
    def print_menu():
        """Display the main menu options."""
        print("\n=== Advanced Mathematics Program ===")
        print("1. Basic Mathematics")
        print("2. Algebra")
        print("3. Calculus")
        print("4. Statistics")
        print("5. Exit")

    @staticmethod
    def basic_math_menu():
        """Handle basic mathematics operations."""
        while True:
            print("\n=== Basic Mathematics ===")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Power")
            print("6. Square Root")
            print("7. Absolute Value")
            print("8. Back")
            
            choice = input("\nEnter your choice (1-8): ")
            
            if choice == '8':
                break
                
            try:
                if choice in ['1', '2', '3', '4', '5']:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                elif choice in ['6', '7']:
                    a = float(input("Enter number: "))
                else:
                    print("Invalid choice!")
                    continue
                    
                if choice == '1':
                    result = BasicMath.add(a, b)
                elif choice == '2':
                    result = BasicMath.subtract(a, b)
                elif choice == '3':
                    result = BasicMath.multiply(a, b)
                elif choice == '4':
                    result = BasicMath.divide(a, b)
                elif choice == '5':
                    result = BasicMath.power(a, b)
                elif choice == '6':
                    result = BasicMath.square_root(a)
                elif choice == '7':
                    result = BasicMath.absolute_value(a)
                
                print(f"\nResult: {result}")
            except ValueError as e:
                print(f"\nError: {str(e)}")
            except ZeroDivisionError:
                print("\nError: Cannot divide by zero!")

    @staticmethod
    def algebra_menu():
        """Handle algebraic operations."""
        while True:
            print("\n=== Algebra ===")
            print("1. Solve Quadratic Equation")
            print("2. Solve System of Linear Equations")
            print("3. Find Polynomial Roots")
            print("4. Matrix Operations")
            print("5. Back")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '5':
                break
                
            try:
                if choice == '1':
                    print("\nEnter coefficients for ax² + bx + c = 0")
                    a = float(input("Enter a: "))
                    b = float(input("Enter b: "))
                    c = float(input("Enter c: "))
                    roots = Algebra.solve_quadratic(a, b, c)
                    print(f"\nRoots: x₁ = {roots[0]}, x₂ = {roots[1]}")
                
                elif choice == '2':
                    n = int(input("\nEnter number of equations: "))
                    coefficients = []
                    constants = []
                    print("\nEnter coefficients row by row:")
                    for i in range(n):
                        row = [float(x) for x in input(f"Row {i+1}: ").split()]
                        coefficients.append(row)
                    print("\nEnter constants:")
                    constants = [float(x) for x in input("Constants: ").split()]
                    solution = Algebra.solve_linear_system(coefficients, constants)
                    print("\nSolution:", solution)
                
                elif choice == '3':
                    coeffs = [float(x) for x in input("\nEnter coefficients (highest degree first): ").split()]
                    roots = Algebra.polynomial_roots(coeffs)
                    print("\nRoots:", roots)
                
                elif choice == '4':
                    print("\nMatrix Operations:")
                    print("1. Addition")
                    print("2. Subtraction")
                    print("3. Multiplication")
                    op_choice = input("Choose operation (1-3): ")
                    
                    rows = int(input("\nEnter number of rows for first matrix: "))
                    cols = int(input("Enter number of columns for first matrix: "))
                    print("\nEnter first matrix elements row by row:")
                    matrix_a = []
                    for i in range(rows):
                        row = [float(x) for x in input(f"Row {i+1}: ").split()]
                        matrix_a.append(row)
                    
                    print("\nEnter second matrix elements row by row:")
                    matrix_b = []
                    for i in range(rows):
                        row = [float(x) for x in input(f"Row {i+1}: ").split()]
                        matrix_b.append(row)
                    
                    op_map = {'1': 'add', '2': 'subtract', '3': 'multiply'}
                    result = Algebra.matrix_operations(matrix_a, matrix_b, op_map[op_choice])
                    print("\nResult:")
                    for row in result:
                        print(row)
                
            except ValueError as e:
                print(f"\nError: {str(e)}")
            except Exception as e:
                print(f"\nError: {str(e)}")

    @staticmethod
    def calculus_menu():
        """Handle calculus operations."""
        while True:
            print("\n=== Calculus ===")
            print("1. Calculate Derivative")
            print("2. Calculate Definite Integral")
            print("3. Calculate Limit")
            print("4. Generate Taylor Series")
            print("5. Back")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '5':
                break
                
            try:
                if choice == '1':
                    print("\nAvailable functions:")
                    print("1. x²")
                    print("2. sin(x)")
                    print("3. e^x")
                    func_choice = input("Choose function (1-3): ")
                    x = float(input("Enter point x: "))
                    
                    if func_choice == '1':
                        f = lambda x: x**2
                    elif func_choice == '2':
                        f = lambda x: np.sin(x)
                    elif func_choice == '3':
                        f = lambda x: np.exp(x)
                    else:
                        print("Invalid function choice!")
                        continue
                        
                    result = Calculus.derivative(f, x)
                    print(f"\nDerivative at x = {x}: {result}")
                
                elif choice == '2':
                    print("\nAvailable functions:")
                    print("1. x²")
                    print("2. sin(x)")
                    print("3. e^x")
                    func_choice = input("Choose function (1-3): ")
                    a = float(input("Enter lower bound a: "))
                    b = float(input("Enter upper bound b: "))
                    
                    if func_choice == '1':
                        f = lambda x: x**2
                    elif func_choice == '2':
                        f = lambda x: np.sin(x)
                    elif func_choice == '3':
                        f = lambda x: np.exp(x)
                    else:
                        print("Invalid function choice!")
                        continue
                        
                    result = Calculus.definite_integral(f, a, b)
                    print(f"\nDefinite integral from {a} to {b}: {result}")
                
                elif choice == '3':
                    print("\nAvailable functions:")
                    print("1. 1/x")
                    print("2. sin(x)/x")
                    func_choice = input("Choose function (1-3): ")
                    x = float(input("Enter point x: "))
                    
                    if func_choice == '1':
                        f = lambda x: 1/x
                    elif func_choice == '2':
                        f = lambda x: np.sin(x)/x if x != 0 else 1
                    else:
                        print("Invalid function choice!")
                        continue
                        
                    result = Calculus.limit(f, x)
                    print(f"\nLimit as x approaches {x}: {result}")
                
                elif choice == '4':
                    print("\nAvailable functions:")
                    print("1. sin(x)")
                    print("2. e^x")
                    func_choice = input("Choose function (1-3): ")
                    x = float(input("Enter x: "))
                    a = float(input("Enter point a (to expand around): "))
                    n = int(input("Enter number of terms: "))
                    
                    if func_choice == '1':
                        f = lambda x: np.sin(x)
                    elif func_choice == '2':
                        f = lambda x: np.exp(x)
                    else:
                        print("Invalid function choice!")
                        continue
                        
                    result = Calculus.taylor_series(f, x, a, n)
                    print(f"\nTaylor series approximation at x = {x}: {result}")
                
            except ValueError as e:
                print(f"\nError: {str(e)}")
            except Exception as e:
                print(f"\nError: {str(e)}")

    @staticmethod
    def statistics_menu():
        """Handle statistical operations."""
        while True:
            print("\n=== Statistics ===")
            print("1. Descriptive Statistics")
            print("2. Correlation Analysis")
            print("3. Hypothesis Testing")
            print("4. Probability Distributions")
            print("5. Confidence Intervals")
            print("6. Back")
            
            choice = input("\nEnter your choice (1-6): ")
            
            if choice == '6':
                break
                
            try:
                if choice == '1':
                    data = [float(x) for x in input("\nEnter data (space-separated): ").split()]
                    stats = Statistics.descriptive_stats(data)
                    print("\nDescriptive Statistics:")
                    for key, value in stats.items():
                        print(f"{key}: {value}")
                
                elif choice == '2':
                    x = [float(x) for x in input("\nEnter first dataset (space-separated): ").split()]
                    y = [float(x) for x in input("Enter second dataset (space-separated): ").split()]
                    corr = Statistics.correlation_analysis(x, y)
                    print("\nCorrelation Analysis:")
                    for key, value in corr.items():
                        print(f"{key}: {value}")
                
                elif choice == '3':
                    print("\nAvailable tests:")
                    print("1. One-sample t-test")
                    print("2. Two-sample t-test")
                    print("3. Wilcoxon signed-rank test")
                    print("4. Mann-Whitney U test")
                    test_choice = input("Choose test (1-4): ")
                    
                    sample1 = [float(x) for x in input("\nEnter first sample (space-separated): ").split()]
                    sample2 = None
                    if test_choice in ['2', '4']:
                        sample2 = [float(x) for x in input("Enter second sample (space-separated): ").split()]
                    
                    test_map = {
                        '1': 't_test',
                        '2': 't_test',
                        '3': 'wilcoxon',
                        '4': 'mann_whitney'
                    }
                    
                    results = Statistics.hypothesis_testing(sample1, sample2, test_map[test_choice])
                    print("\nHypothesis Test Results:")
                    for key, value in results.items():
                        print(f"{key}: {value}")
                
                elif choice == '4':
                    print("\nAvailable distributions:")
                    print("1. Normal")
                    print("2. Uniform")
                    print("3. Poisson")
                    dist_choice = input("Choose distribution (1-3): ")
                    
                    params = {}
                    if dist_choice == '1':
                        params['mu'] = float(input("Enter mean (mu): "))
                        params['sigma'] = float(input("Enter standard deviation (sigma): "))
                        dist_type = 'normal'
                    elif dist_choice == '2':
                        params['a'] = float(input("Enter lower bound (a): "))
                        params['b'] = float(input("Enter upper bound (b): "))
                        dist_type = 'uniform'
                    elif dist_choice == '3':
                        params['mu'] = float(input("Enter mean (mu): "))
                        dist_type = 'poisson'
                    else:
                        print("Invalid distribution choice!")
                        continue
                    
                    x, y = Statistics.probability_distribution(dist_type, **params)
                    print("\nDistribution values (x, p(x)):")
                    for i in range(min(10, len(x))):
                        print(f"{x[i]}: {y[i]}")
                
                elif choice == '5':
                    data = [float(x) for x in input("\nEnter sample data (space-separated): ").split()]
                    confidence = float(input("Enter confidence level (0-1): "))
                    lower, upper = Statistics.confidence_interval(data, confidence)
                    print(f"\nConfidence Interval: ({lower}, {upper})")
                
            except ValueError as e:
                print(f"\nError: {str(e)}")
            except Exception as e:
                print(f"\nError: {str(e)}")

    @staticmethod
    def run():
        """Run the main program loop."""
        while True:
            MathProgram.print_menu()
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '5':
                print("\nThank you for using the Advanced Mathematics Program!")
                break
            elif choice == '1':
                MathProgram.basic_math_menu()
            elif choice == '2':
                MathProgram.algebra_menu()
            elif choice == '3':
                MathProgram.calculus_menu()
            elif choice == '4':
                MathProgram.statistics_menu()
            else:
                print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    print("Welcome to the Advanced Mathematics Program!")
    print("This program provides various mathematical tools from basic arithmetic to college-level mathematics.")
    MathProgram.run()
