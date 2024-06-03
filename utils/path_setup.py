import os
import sys

class PathSetup:
    @staticmethod
    def add_project_root_to_sys_path():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        if project_root not in sys.path:
            sys.path.insert(0, project_root)  # Insert at the beginning of sys.path
