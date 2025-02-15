# Advanced Mathematics Program

A comprehensive mathematics program that provides tools for basic arithmetic through college-level mathematics, including algebra, calculus, and statistics.

## Features

### Basic Mathematics
- Addition, subtraction, multiplication, division
- Power and square root calculations
- Absolute value

### Algebra
- Quadratic equation solver
- System of linear equations solver
- Polynomial root finder
- Matrix operations (addition, subtraction, multiplication)

### Calculus
- Numerical derivatives
- Partial derivatives
- Definite integrals (multiple methods)
- Limits
- Taylor series expansions

### Statistics
- Descriptive statistics (mean, median, mode, standard deviation, etc.)
- Correlation analysis (Pearson and Spearman)
- Hypothesis testing
  - One-sample t-test
  - Two-sample t-test
  - Wilcoxon signed-rank test
  - Mann-Whitney U test
- Probability distributions
  - Normal distribution
  - Uniform distribution
  - Poisson distribution
- Confidence intervals

## Installation

1. Ensure you have Python 3.7 or higher installed
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/math_program.git
   cd math_program
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the program:
```bash
python main.py
```

The program provides an interactive menu-driven interface where you can:
1. Choose the mathematical domain (Basic Math, Algebra, Calculus, or Statistics)
2. Select specific operations within each domain
3. Input your data
4. View the results

### Example Usage

#### Basic Mathematics
```python
# Using the BasicMath class directly
from basic_math import BasicMath

result = BasicMath.add(5, 3)  # Returns 8
result = BasicMath.power(2, 3)  # Returns 8
```

#### Algebra
```python
# Solving a quadratic equation
from algebra import Algebra

# Solve x² + 2x + 1 = 0
roots = Algebra.solve_quadratic(1, 2, 1)  # Returns (-1, -1)
```

#### Calculus
```python
# Calculate derivative
from calculus import Calculus
import math

# Calculate derivative of sin(x) at x = 0
result = Calculus.derivative(math.sin, 0)  # Returns approximately 1.0
```

#### Statistics
```python
# Calculate descriptive statistics
from statistics import Statistics

data = [1, 2, 3, 4, 5]
stats = Statistics.descriptive_stats(data)
```

## Documentation

### Module Structure
- `basic_math.py`: Basic arithmetic operations
- `algebra.py`: Algebraic calculations and equation solving
- `calculus.py`: Calculus operations (derivatives, integrals, limits)
- `statistics.py`: Statistical analysis and probability functions
- `main.py`: Main program interface

### Error Handling
The program includes comprehensive error handling for:
- Invalid input types
- Division by zero
- Invalid matrix dimensions
- Non-real solutions
- Statistical computation errors

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Requirements

- Python 3.7+
- NumPy
- SciPy

See `requirements.txt` for specific version requirements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

Your Name - Initial work

## Acknowledgments

- NumPy team for numerical computing tools
- SciPy team for scientific computing libraries
