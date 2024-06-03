from utils import PathSetup
PathSetup.add_project_root_to_sys_path()

from scripts.example_script import do_something

if __name__ == "__main__":
    do_something()
