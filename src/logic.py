"""
Core business logic.
Handles wash duration timing, wagon speed calculation, and queue managment.
"""

from time import time, sleep
def wagon_speed_kmh():
    """Calculates wagon speed in km/h from its length and wash duration."""
    wagon_length = 25 # Wagon length in meters

    start_of_the_washing_time = time()

    sleep(5)

    end_of_the_washing_time = time()

    total_time = end_of_the_washing_time - start_of_the_washing_time

    railway_speed = (wagon_length / total_time) * 3.6

    print("Скорость мойки пройденного вагона равна", round(railway_speed), "км/ч.")

wagon_speed_kmh()