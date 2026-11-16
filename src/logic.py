"""
Core business logic.
Handles wash duration timing, wagon speed calculation, and queue managment.
"""

# Imports
from time import perf_counter


### FUNCTIONS

def start_timer():
    """Records the current start time."""
    start_time = perf_counter()
    return start_time

def stop_timer(start_time):
    """Records the current end time."""
    end_time = perf_counter()
    duration = end_time - start_time
    return duration

def calculate_speed(duration):
    """Calculates the speed of the wagon duration."""
    # Variables
    wagon_length = 25 # In meters
    wagon_speed = (wagon_length / duration) * 3.6 # In km/h

    return wagon_speed