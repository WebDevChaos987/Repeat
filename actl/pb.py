import sys
from .wait import wait
from .color import color

def progress_bar(duration=10, bar_color="green"):
    """
    Displays an animated text-based progress bar that grows over time.
    """
    slots = 20  # Total length of the bar blocks
    
    for i in range(slots + 1):
        percent = int((i / slots) * 100)
        filled = "|" * i
        empty = ":" * (slots - i)
        
        # Build the bar string
        bar_text = f"\rProgress: [{filled}{empty}] {percent}%"
        
        # Color the bar and print it out dynamically
        sys.stdout.write(color(bar_text, bar_color))
        sys.stdout.flush()
        
        # Wait a bit before loading the next block
        # (Dividing duration into small slices for each block)
        wait(int(duration * 20000)) 
    print()  # Jumps to the next line when finished
