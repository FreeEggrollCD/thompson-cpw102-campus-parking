# Engineering Design

**Project:** Campus Parking Helper  
**Team members:** Jonathon Thompson
**Date:** 30 Sep 26

## Problem Summary
Calculating thee price of parking is inconvenient and slow to calculate by hand.

## Proposed solution
Create a python program to calculate the cost of parking per hour.

## Technical design

### Inputs
_What data and information will go into the program? What data types will the program use to represent that data?_
The estimated parking time and price will be needed, these will be parsed as floats.

### Processing
_What will the program do with the data? What calculations will it perform?_ 
The parameters will be passed into a function that uses the equation `p=h*r` where 'h' is hours, 'r' is the price per hour, and 'p' is the total cost.

### Output
_What will the program return or print to the user?_
The output will be another floating point representing the dollar ammount to be charged for the amount of time parked.

### Functions
_What function(s) could this program use to modularize the logic? What actions belong together?_
I will make a function called `parkingCost()` to do the afformentiond calculation to return the cost of parking.

## Example interaction

```text
User input: 3 hours at $2.00/hr

Program output: Total cost of parking is $6.00
```

## Implementation plan

1. 
2. 
3. 

