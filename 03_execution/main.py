# Get configuration from file
def init():
    with open("config.conf") as conf:
        price = conf.readline()

# Function to calculate cost of parking
def parkingCost(hours:float, rate:float) -> float:
    """
    Calculates cost of parking

    `params:`
      hours(float): Amount of time for parking
      rate(float): Price per hour for parking
    `returns:`
      cost(float): Cost of parking according to hours*rate
    """
    
    cost:float = hours*rate
    return cost

def main(price:float):
    print("How many hours are you going to be parked?")
    initial_input = input()
    try:
        hours:float = float(initial_input)
        total:float = parkingCost(hours, price)
        print(f"Your cost will be ${total:.2f}")
    except ValueError:
        print("Please enter a number.")

if __name__ == "__main__":
    price:float = 2.00
    main(price)