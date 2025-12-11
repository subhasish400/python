''' Devlope a python program which uses two thread among them one print numbers and the other one letters. They finished faster than running alone, showing how multithreading improves speeds as well as efficiency.'''
# Here we are going to perform the multithreading operation
import threading
import time
from datetime import datetime
# Now we are going to create two different functions
# Here the first function is nothing but it prints the first 5 natural numbers
def print_number():
    for i in range(5):
        time.sleep(2)   # Here we have given sleep time for 2 second just because after two second only new character should be apprar.
        print(f"Number: {i}")
# The second function is nothing but to print the first 5 letters
def print_letter():
    letters = 'abcde'
    for letter in letters:
        time.sleep(2)
        print(f"letter: {letter}")
# Now we are going to create two threads for the respective functions so we have
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)
start_time = datetime.now().strftime("%H:%M:%S")
print(f'The peocess begins')
print(f'The process started in\n{start_time}')
t1.start()
t2.start()
# Now we are going to join the respective threads
t1.join()
t2.join()
print(f'Process got finished')
End_time = datetime.now().strftime("%H:%M:%S")
print(f'Process ended in\n {End_time}')
