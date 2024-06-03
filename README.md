## Setting Up Your Python Project Environment: A Comprehensive Guide

When starting a new Python project, setting up a clean and organized environment is crucial for maintaining your code and managing dependencies. In this blog, we'll walk through the steps to set up your Python project environment using either `pip` or `conda`, including creating a virtual environment, installing essential libraries, and ensuring reproducibility. We'll also introduce a basic folder structure, utility classes for managing environment variables and logging, and instructions for setting up version control with Git.

### Folder Structure

First, let's define a basic folder structure for your project. This will help keep your code organized and make it easier to manage as your project grows.

```
project_root/
│
├── utils/
│   ├── env_manager.py
│   └── logging_wrapper.py
│
├── notebooks/
│   └── example_notebook.ipynb
│
├── scripts/
│   └── example_script.py
│
├── data/
│   └── example_data.csv
│
├── models/
│   └── example_model.pkl
│
├── .env
├── environment.yml
├── requirements.txt
├── .gitignore
└── README.md
```

### Installation Instructions

To get started with your Python project, follow these steps to set up the necessary environment and install essential packages.

#### Using pip

1. **Upgrade pip**

   Ensure you have the latest version of pip installed to avoid compatibility issues:

   ```sh
   python -m pip install --upgrade pip
   ```

2. **Create a Virtual Environment**

   Create a virtual environment to manage dependencies separately from your system Python installation:

   ```sh
   python -m venv project-env
   ```

3. **Activate the Virtual Environment**

   Activate the virtual environment you just created:

   - On Windows:

     ```sh
     .\project-env\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source project-env/bin/activate
     ```

4. **Install Required Packages**

   Install basic libraries within the virtual environment:

   ```sh
   pip install numpy pandas matplotlib jupyter ipykernel python-dotenv
   ```

5. **Generate `requirements.txt`**

   Save the installed packages to a `requirements.txt` file:

   ```sh
   pip freeze > requirements.txt
   ```

6. **Install Dependencies Using `requirements.txt`**

   If setting up on another machine, install the dependencies from `requirements.txt`:

   ```sh
   pip install -r requirements.txt
   ```

#### Using conda

1. **Create a New Conda Environment**

   Create a new conda environment with Python 3.10:

   ```sh
   conda create -n project-env python=3.10 -y
   ```

2. **Activate the Conda Environment**

   Activate the newly created environment:

   ```sh
   conda activate project-env
   ```

3. **Install Required Packages**

   Install basic libraries using conda-forge:

   ```sh
   conda install -c conda-forge numpy pandas matplotlib jupyter ipykernel python-dotenv -y
   ```

4. **Generate `environment.yml`**

   Export the environment to an `environment.yml` file:

   ```sh
   conda env export -n project-env > environment.yml
   ```

5. **Install Environment Using `environment.yml`**

   If setting up on another machine, create the environment from `environment.yml`:

   ```sh
   conda env create -f environment.yml
   ```

### Setting Up Git

1. **Initialize Git Repository**

   Initialize a new Git repository in your project directory:

   ```sh
   git init
   ```

2. **Create a `.gitignore` File**

   Create a `.gitignore` file to exclude files and directories that you don't want to track in version control:

   ```plaintext
   # Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
   ```

3. **Add and Commit Files**

   Add and commit your files to the Git repository:

   ```sh
   git add .
   git commit -m "Initial commit"
   ```

### Utility Classes

#### env_manager.py

This utility class helps manage environment variables, making it easier to handle configurations.

```python
# utils/env_manager.py
import os
import sys
from dotenv import load_dotenv
from utils.logging_wrapper import LoggingWrapper

logger = LoggingWrapper(__name__)

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

            # Add the project root to sys.path
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if project_root not in sys.path:
                sys.path.append(project_root)
                logger.info(f"Added {project_root} to sys.path")

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
```

#### logging_wrapper.py

This utility class provides a simple wrapper around Python's logging module, allowing for consistent and configurable logging throughout your project.

```python
# utils/logging_wrapper.py
import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

class LoggingWrapper:
    """
    A wrapper for the Python logging module that sets up logging to both a file and the console.

    Attributes:
        logger (logging.Logger): The logger instance.
    """

    def __init__(self, name, log_dir='logs', log_level=logging.DEBUG, console_level=logging.ERROR, max_bytes=5*1024*1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        if not os.path.exists(log_dir):
            os

.makedirs(log_dir)
        
        now = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = os.path.join(log_dir, f'log_{now}.log')
        fh = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        fh.setLevel(log_level)
        fh.setFormatter(formatter)
        
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
    
    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)
    
    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)
    
    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)
    
    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)
    
    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)
```

### Example Script

Here's a toy example for `example_script.py` that utilizes the utility classes (`EnvManager` and `LoggingWrapper`) to demonstrate their benefits. The script will read an environment variable, perform a simple calculation, log the results, and include error handling.

```python
# scripts/example_script.py

import os
from utils.env_manager import EnvManager
from utils.logging_wrapper import LoggingWrapper

# Initialize logging
logger = LoggingWrapper(__name__).get_logger()

# Initialize environment manager and load .env variables
env_manager = EnvManager()

def main():
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

if __name__ == "__main__":
    main()
```

### Sample `.env` File

Make sure your `.env` file contains the following entries for the example to work:

```plaintext
# .env
NUMBER1=15
NUMBER2=25
```

### Dependencies List

- `numpy`
- `pandas`
- `matplotlib`
- `jupyter`
- `ipykernel`
- `python-dotenv`

### Additional Steps

- **Verify Installation**

   Ensure all packages are installed correctly by starting a Jupyter notebook:

   ```sh
   jupyter notebook
   ```

- **Updating the Environment**

   To update the environment with new packages, install them and regenerate the `requirements.txt` or `environment.yml` file as appropriate.

   For pip:
   ```sh
   pip install <new-package>
   pip freeze > requirements.txt
   ```

   For conda:
   ```sh
   conda install -c conda-forge <new-package> -y
   conda env export -n project-env > environment.yml
   ```

### Conclusion

Setting up a well-organized Python project environment is essential for efficient development and collaboration. By following these steps and using the provided utility classes and folder structure, you can ensure your project remains manageable and reproducible. Whether you prefer `pip` or `conda`, these instructions will help you get started quickly and maintain a clean environment for your Python projects.