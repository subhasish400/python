'''Write a program in python to demonstrate parallel execution using ProcessPoolExecutor, measure start as well as end time,compute squares concurrently,understand multiprocessing rules and avoid common mistakes like non-pickable functions in python windows systems clearly enviornment.'''
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
import time

def square(n):
    time.sleep(1)
    return f"Square : {n * n}"

def print_squares(numbers):
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)
        for result in results:
            print(result)

if __name__ == "__main__":
    numbers = [x for x in range(1, 11)]
    start_time = datetime.now().strftime("%H:%M:%S")
    t = time.time()
    print(f'The process started at\n{start_time}')

    print_squares(numbers)

    end_time = datetime.now().strftime("%H:%M:%S")
    print(f'The process ended at\n{end_time}')
    t2 = time.time() - t
    print(f'The total time taken by the process becomes:\n{t2}')
