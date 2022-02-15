import os
from pathlib import Path
from router_data import RTFile


class RTPath:
    def __init__(self, dir: Path) -> None:
        self._files = dict()

        self._dir = dir
        self._original_dir = Path(os.getcwd())
        self._current_dir = self._original_dir

    def append(self, file: RTFile) -> None:
        self._files[file.name] = file

    def remove(self, file_name: str) -> None:
        del self._files[file_name]

    def get_file(self, file_name: str) -> RTFile:
        return self._files[file_name]

    def go(self) -> None:
        try:
            os.chdir(self._dir)
        except FileNotFoundError:
            os.mkdir(self._dir)
            os.chdir(self._dir)

        self._current_dir = self._dir

    def goback(self) -> None:
        os.chdir(self._original_dir)
        self._current_dir = self._original_dir

    def get_current_dir(self) -> str:
        return str(self._current_dir)
