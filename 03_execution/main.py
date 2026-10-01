#!/usr/bin/env python3

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
    options = init()
    price:float = options["price"]
    initial_input = input("How many hours are you going to be parked?: ")
    try:
        hours:float = float(initial_input)
        total:float = parkingCost(hours, price)
        print(f"Your estimated cost is ${total:.2f}")
    except ValueError:
        print("Please enter a number.")

if __name__ == "__main__":
    main()