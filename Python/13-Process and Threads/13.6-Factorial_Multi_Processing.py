'''
Real-World example: Multiprocessing for CPU-Bound tasks
Scenario: Factorial Calculation
Factorial Calculation, Especially for large numbers,
involve significant computational work. Multiprocessing can be used
to distribute the workload across multiple CPU Scores, improving performances.
'''
import multiprocessing
import math
import sys
import time
## Increasse the maximum number digit for integer conversion
sys.set_int_max_str_digits(100000)
## function to compute factorails of a given number
def computer_factorial(number):
    print(f"computing factorial of a {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result
if __name__ == "__main__":
    numbers = [5,10,12,15,20]
    start_time = time.time()
    ## create a pool of worker processes
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(computer_factorial, numbers)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")