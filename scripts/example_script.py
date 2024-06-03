# Now import the necessary modules
from utils import EnvManager, LoggingWrapper

# Initialize logging
logger = LoggingWrapper(__name__).logger

# Initialize environment manager and load .env variables
env_manager = EnvManager()

def do_something():
    try:
        # Get environment variables
        number1 = env_manager.get_env_variable('NUMBER1', '10')
        number2 = env_manager.get_env_variable('NUMBER2', '5')
        
        # Convert to integers
        num1 = int(number1)
        num2 = int(number2)

        logger.info(f"Retrieved environment variables: NUMBER1={num1}, NUMBER2={num2}")

        # Perform a simple calculation
        result = num1 + num2
        logger.info(f"The result of adding {num1} and {num2} is {result}")

    except ValueError as e:
        logger.error(f"Error converting environment variables to integers: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")