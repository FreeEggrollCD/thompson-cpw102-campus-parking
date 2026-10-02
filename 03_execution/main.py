#!/usr/bin/env python3
import time

# Clear screen command
clear = lambda: print("\033[H\033[2J", end="")

# Get configuration from file
def init() -> dict:
    """
    Loads configuration from config.ini into a dictionary

    Currently only designed to load floats.

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
    max_hours = options["max_hours"]
    total_time_seconds:float = 0
    return_cost:bool = True

    # Looping until a valid input is given
    while estimating:
        clear()
        initial_input = input("How many hours are you going to be parked?: ")
        try:
            hours:float = float(initial_input)
            if hours > max_hours or hours <= 0:
                raise RuntimeError("Unreasonable amount of hours")
            total:float = parkingCost(hours, price)
            print(f"Your estimated cost is ${total:.2f}")
            estimating = False
        except ValueError:
            input(f"Please enter a number. (press enter to try again)")
        except RuntimeError:
            input(f"Please enter a reasonable number of hours. (press enter to try again)")
    while waiting:
        try:
            time.sleep(1)
            total_time_seconds += 1
            if total_time_seconds / 3600 > max_hours:
                raise RuntimeError("Unreasonable amount of time")
        except KeyboardInterrupt:
            total_time_hours:float = total_time_seconds / 3600
            print(f"\rYou have been parked for {total_time_hours:.2f} hours.")
            waiting = False
        except RuntimeError:
            print("You have been parked for an unreasonable amount of time. Alerting staff.")
            waiting = False
            return_cost = False
    if return_cost:
        total_time_hours:float = total_time_seconds / 3600
        if total_time_hours > hours:
            print(f"You have exceeded your estimated time by {total_time_hours - hours:.2f} hour(s).")
        total:float = parkingCost(total_time_hours, price)
        print(f"Your total cost is ${total:.2f}")

if __name__ == "__main__":
    main()