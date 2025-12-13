'''
Devlope a program in python to create a function such that it takes a list on numbers as input from the user and measures how long multithreading program runs,record the start and end times using time.time(), substract them and print only the execution duration in seconds.
'''
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
def print_numbers(numbers):
    def print_number(numbers):
        time.sleep(1)
        return f"Number : {numbers}"
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_number,numbers)
    for result in results:
        print(result)
        
numbers = [x for x in range(1,21)]
if __name__ == '__main__':
    start_time = datetime.now().strftime("%H:%M:%S")
    t1 = time.time()
    print(f'The process started at\n {start_time}')
    print_numbers(numbers)
    end_time = datetime.now().strftime("%H:%M:%S")
    print(f'The process ends at\n {end_time}')
    t2 = time.time() - t1
    print(f'The total time taken by the process becomes:\n {t2}')
    