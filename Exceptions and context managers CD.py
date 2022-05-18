import os


class Cd:
    def __init__(self, new_path: str) -> None:
        self.new_path = new_path

    def __enter__(self) -> None:
        if (not os.path.exists(self.new_path) or 
            not os.path.isdir(self.new_path)):
            raise ValueError
        self.old_dir = os.getcwd()
        os.chdir(self.new_path)
        return None

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        os.chdir(self.old_dir)
        del self.old_dir
        del self.new_path
