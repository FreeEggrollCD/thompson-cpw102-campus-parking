#!/usr/bin/env python3
import sys
import time

# Clear screen command
clear = lambda: print("\033[H\033[2J", end="")

# Get configuration from file
def init() -> dict:
    """
    Loads configuration from config.ini into a dictionary

    Arbitrary options can be added to the config.ini file but
    \n can only be used if the code is extended to handle them.
    \n They will be ignored otherwise.

    Returns:
        dict: Configuration options
    """

    config = {}
    with open("config.ini") as conf:
        for line in conf:
            if not line or "=" not in line:
                continue
            option, value = line.split("=")
            config[option.strip()] = float(value.strip())
    return config

# Function to calculate cost of parking
def parkingCost(hours:float, rate:float) -> float:
    """
    Calculates cost of parking

    Args:
      hours (float): Amount of time for parking
      rate (float): Price per hour for parking
    Returns:
      float: Cost of parking according to hours*rate as 'cost'
    Raises:
        ValueError: If hours is not a number
    """
    
    cost:float = hours*rate
    return cost

def main():
    # Variable declarations
    estimating:bool = True
    waiting:bool = True
    options:dict = init()
    price:float = options["rate"]
    too_big = sys.float_info.max
    total_time_seconds:float = 0
    return_cost:bool = True

    # Looping until a valid input is given
    while estimating:
        clear()
        initial_input = input("How many hours are you going to be parked?: ")
        try:
            hours:float = float(initial_input)
            if hours > too_big or hours < 0:
                raise RuntimeError("Unreasonable amount of hours")
            total:float = parkingCost(hours, price)
            print(f"Your estimated cost is ${total:.2f}")
            estimating = False
        except ValueError:
            input(f"Please enter a number. (press enter to try again)")
        except RuntimeError:
            input(f"Please enter a reasonable number of hours. (press enter to try again)")


if __name__ == "__main__":
    main()