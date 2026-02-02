from __future__ import annotations
from fastmcp import FastMCP
import math
import statistics

mcp = FastMCP("Advanced Math Server")

def _as_number(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise TypeError("Expected a number (int/float or numeric string)")

# ---------------- BASIC OPERATIONS ---------------- #

@mcp.tool()
async def add(a: float, b: float) -> float:
    return _as_number(a) + _as_number(b)

@mcp.tool()
async def subtract(a: float, b: float) -> float:
    return _as_number(a) - _as_number(b)

@mcp.tool()
async def multiply(a: float, b: float) -> float:
    return _as_number(a) * _as_number(b)

@mcp.tool()
async def divide(a: float, b: float) -> float:
    b = _as_number(b)
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return _as_number(a) / b

@mcp.tool()
async def modulus(a: float, b: float) -> float:
    return _as_number(a) % _as_number(b)

# ---------------- POWER & ROOT ---------------- #

@mcp.tool()
async def power(a: float, b: float) -> float:
    return _as_number(a) ** _as_number(b)

@mcp.tool()
async def sqrt(a: float) -> float:
    a = _as_number(a)
    if a < 0:
        raise ValueError("Square root of negative number is not allowed")
    return math.sqrt(a)

@mcp.tool()
async def cube_root(a: float) -> float:
    return _as_number(a) ** (1/3)

# ---------------- ADVANCED MATH ---------------- #

@mcp.tool()
async def factorial(n: int) -> int:
    n = int(_as_number(n))
    if n < 0:
        raise ValueError("Factorial of negative number not allowed")
    return math.factorial(n)

@mcp.tool()
async def gcd(a: int, b: int) -> int:
    return math.gcd(int(a), int(b))

@mcp.tool()
async def lcm(a: int, b: int) -> int:
    return abs(int(a * b)) // math.gcd(int(a), int(b))

# ---------------- TRIGONOMETRY ---------------- #

@mcp.tool()
async def sin(x: float) -> float:
    return math.sin(_as_number(x))

@mcp.tool()
async def cos(x: float) -> float:
    return math.cos(_as_number(x))

@mcp.tool()
async def tan(x: float) -> float:
    return math.tan(_as_number(x))

# ---------------- LOGARITHMS ---------------- #

@mcp.tool()
async def log(x: float, base: float = math.e) -> float:
    return math.log(_as_number(x), _as_number(base))

@mcp.tool()
async def log10(x: float) -> float:
    return math.log10(_as_number(x))

# ---------------- STATISTICS ---------------- #

@mcp.tool()
async def mean(numbers: list[float]) -> float:
    return statistics.mean(numbers)

@mcp.tool()
async def median(numbers: list[float]) -> float:
    return statistics.median(numbers)

@mcp.tool()
async def variance(numbers: list[float]) -> float:
    return statistics.variance(numbers)

@mcp.tool()
async def std_dev(numbers: list[float]) -> float:
    return statistics.stdev(numbers)

# ---------------- START SERVER ---------------- #

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
