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
        name = file.get_name()
        self._files[name] = file

    def remove(self, file: str) -> None:
        del self._files[file]

    def go(self) -> None:
        os.chdir(self._dir)
        self._current_dir = self._dir

    def goback(self) -> None:
        os.chdir(self._original_dir)
        self._current_dir = self._original_dir

    def get_current_dir(self) -> str:
        return str(self._current_dir)
