# Now we are going to calculate factorial for especially large numbers, involve signifiant computational work, so multiprocessing can be used to distribute the workload accross multiple cpu cores for improving performance.

import multiprocessing
import time
import sys
from datetime import datetime

# Now we are going to set the maximum range so we have 
sys.set_int_max_str_digits(10000)

# Now we are going to define a function to calculate factorial
def calculate_factorial(num):
    if num < 0:
        return f'Factorial not possible'
    if num == 0:
        return 1
    else:
        fact = 1
        for i in range(2,num + 1):
            fact = fact * i
        return fact
    
# Now we are going to create some entry point so we have
if __name__ == '__main__':
    numbers = [x*100 for x in range(1,6)]
    start_time = datetime.now().strftime("%H:%M:%S")
    t1 = time.time()
    print(f'Process started at\n {start_time}')
    # Now we are going to create a pool of worker processes so we have
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial,numbers)
    end_time = datetime.now().strftime("%H:%M:%S")
    t2 = time.time() - t1
    print(f'The result becomes:\n {results}')
    print(f'The process has been completed at\n {end_time}')
    print(f'The time taken by the process to be complete becomes:\n {t2}')
        