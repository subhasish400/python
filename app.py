# Here we are going to develope a simple application which consists of an arithematic operation and display the logs
# STEP-1:
# first we are going to import the logging module
import logging
# Noe we have to configure the logging for the debug
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt= '%Y - %m - %d %H : %M : %S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
# Sep-2:
# Here we are going to save all the log messages into a perticular file.
logger = logging.getLogger('ArithematicApp')
# Step-3:
# Now we are going to define several functions for the logging operations
def add(a,b):
    result = a + b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result
def sub(a,b):
    result = a - b
    logger.debug(f'Adding {a} - {b} = {result}')
    return result
def mul(a,b):
    result = a * b
    logger.debug(f'Adding {a} * {b} = {result}')
    return result
def div(a,b):
    try:
        result = a / b
        logger.debug(f'Adding {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
# first we are going to test a function which thakes a number as input parameter from the user and returns it's factorial
def factorial(n):
    logging.debug('Operation is taking place')
    if n < 0:
        return f'Factorial of {n} is not possible'
    elif n == 0:
        return f'Factorial of {n} becomes {1}'
    else:
        return f'Factorial of {n} becomes {n*factorial(n-1)}'
# # Simillarly we are going to create a function such that it returns the addition of two numbers and display the respective logs for it
def addition(a,b):
    logging.debug('Operation is taking place')
    return a+b
# Step-4:
# Now we are going to call the sort of functions whatever we have defined earlier
add(10,15)
sub(15,10)
mul(10,5)
div(10,5)
logging.debug("The factorial function is called")
factorial(5)
logging.debug("The addition function is called")
addition(10,20)
    