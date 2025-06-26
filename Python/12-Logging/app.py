import logging 
## logging settings 
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    handlers=[
        logging.fileHandler("app1.log"),
        logging.streamHandler()
    ]
)
logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"adding {a} + {b} =  {result}")
    return result
def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result
def multiply(a,b):
    result = a*b
    logger.debug(f"MUltiplying {a} * {b} = {result}")
    return result
def divide(a,b):
    try:
        result = a/b
        logger.debug("Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
add(10,15)
subtract(15,10)
multiply(10,20)
divide(20,10)