import os


def set_dag_id(module_path: str):
    return os.path.basename(module_path).replace(".py", "").replace("_", "-")
