import random
from fastmcp import FastMCP

# create a fastmcp server instance
mcp = FastMCP(name="Demo server ")

@mcp.tool()
def roll_dice(n_dics:int=1)->list[int]:
    """Roll n dices and return the result as a list of integers."""
    return [random.randint(1, 6) for _ in range(n_dics)]

@mcp.tool()
def add_numbers(a:int, b:int)->int:
    """ Add two numbers  """
    return a+b

if __name__ == "__main__":
    mcp.run()