import time
from .color import color

def roll(sides=6, dice_color="yellow"):
    """
    Rolls a custom dice without using the random module!
    Uses the system clock microseconds for pseudo-random calculations.
    """
    # 1. Grab the current time in nanoseconds/microseconds (a huge number)
    # Example: 171829384729384
    seed = time.time_ns()
    
    # 2. Use the modulo operator (%) to fit the huge number into our dice size
    # Adding 1 ensures a 6-sided die rolls 1-6 instead of 0-5
    result = (seed % sides) + 1
    
    # 3. Print out a beautifully styled dice message
    dice_msg = f"[:] You rolled a {result}!"
    print(color(dice_msg, dice_color))
    
    return result
