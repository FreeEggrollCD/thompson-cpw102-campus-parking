# Test Cases

## Test Case 1: Valid Input

**Input / Action:**  
Enter 12.

**Expected Result:**  
The program calculates and displays the estimated cost and starts a stopwatch and waits for  
a `KeyboardInterupt` to stop it. The total cost and time waited are then displayed.  
Ohterwise, it stops at the maximum configured time.

**Actual Result:**  
Program calculates `$24.00` as the estimated cost and waits for `KeyboardInterupt`.  
The `KeyboardInterupt` is received and the program displays the total time elapsed and the cost of the  
total time waited.

**Result:**  
Pass

---

## Test Case 2: Boundary Input

**Input / Action:**  
Enter the minimum or maximum allowed float value.

**Expected Result:**  
The program should prompt the user to enter a valid value.

**Actual Result:**  
Program prompts the user to enter a valid value until one is given.

**Result:**  
Pass

---

## Test Case 3: Invalid Input

**Input / Action:**  
Enter a non-float value.

**Expected Result:**  
The program should prompt the user to enter a valid value.

**Actual Result:**  
The program prompts the user to enter a valid value until one is given.

**Result:**  
Pass
