'''Devlope a python program which uses multiprocessing to run two processes simultaneously where one calculates the square and another one calculate the cube within a certain range of numbers where the range is given by the user and measures the start as well as end times to demonstrate parallel execution efficiency.'''
import multiprocessing
import time 
from datetime import datetime
# Now we are going to create two functions that holds two different processes such that one function returns the squares of numbers within a particular range given by the userand other one returns the cude.
def print_squares(n):
    for i in range(n):
        time.sleep(1)
        print(f'Square of {i} becomes: {i**2}')
def print_cubes(n):
    for i in range(n):
        time.sleep(1.5)
        print(f'cube of {i} becomes: {i**3}')
# Now we are going to create two processes for these certain functions so we have
if __name__ == '__main__':
    n = eval(input('Enter the range:'))
    p1 = multiprocessing.Process(target=print_squares,args=(n,))
    p2 = multiprocessing.Process(target=print_cubes,args=(n,))
    start_time = datetime.now().strftime("%H:%M:%S")
    t1 = time.time()
    print(f'The process started at\n {start_time}')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = datetime.now().strftime("%H:%M:%S")
    t2 = time.time() - t1
    print(f'The Process ended at\n {end_time}')
    print(f'Process has been complets in {t2}')
