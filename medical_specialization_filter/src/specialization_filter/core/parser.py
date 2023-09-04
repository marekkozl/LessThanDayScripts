import typing
from pathlib import Path

import pandas

from specialization_filter.core.specialization import Specialization


class Parser:
    def __init__(self, input_directory: Path):
        self.input_directory = input_directory
        self.data = self.init_data()
        self.specializations: typing.List[Specialization] = []

    def get_name(self) -> str:
        pass

    def get_delimiter(self) -> str:
        return ";"

    def init_data(self):
        return pandas.read_csv(
            self.input_directory / self.get_name(), delimiter=self.get_delimiter()
        )
