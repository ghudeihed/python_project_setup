import os
from dotenv import load_dotenv
from utils.logging_wrapper import LoggingWrapper

logger = LoggingWrapper(__name__).logger

class EnvManager:
    """
    A singleton class to manage environment variables and the PYTHONPATH setup.

    This class ensures that environment variables are loaded from a .env file
    and the project root is added to the PYTHONPATH. It uses the singleton pattern
    to ensure the environment is loaded only once.
    """
    
    _instance = None
    _env_loaded = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EnvManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, file_path: str = '.env'):
        if not self._env_loaded:
            self.load_env(file_path)

    def load_env(self, file_path: str) -> None:
        if not EnvManager._env_loaded:
            try:
                if load_dotenv(file_path):
                    logger.info(f"Environment variables loaded from {file_path}")
                else:
                    logger.warning(f"No environment variables found in {file_path}")
                EnvManager._env_loaded = True
            except Exception as e:
                logger.error(f"Error loading environment variables from {file_path}: {e}")
                raise RuntimeError(f"Failed to load environment variables from {file_path}") from e

    @staticmethod
    def get_env_variable(name: str, default: str = None) -> str:
        try:
            value = os.getenv(name, default)
            if value is None:
                logger.warning(f"Environment variable {name} not found, using default value: {default}")
            return value
        except Exception as e:
            logger.error(f"Error getting environment variable {name}: {e}")
            raise RuntimeError(f"Failed to get environment variable {name}") from e
