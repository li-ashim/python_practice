import os
import uuid
import shutil


class TempDir:
    def __init__(self) -> None:
        self.tmpdir_name = str(uuid.uuid4().hex)
        self.old_dir = os.getcwd()

    def __enter__(self) -> None:
        os.mkdir(self.tmpdir_name)
        os.chdir(self.tmpdir_name)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        os.chdir(self.old_dir)
        shutil.rmtree(self.tmpdir_name)
        del self.old_dir
        del self.tmpdir_name
