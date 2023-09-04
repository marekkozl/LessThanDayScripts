import typing
from pathlib import Path

import pandas

from specialization_filter.core.specialization import Specialization
from specialization_filter.parsers.place_parser import PlaceParser


class DataFrameParser:
    def __init__(self, place_parser: PlaceParser):
        self.place_parser = place_parser
        self.data = {
            "Wojewodztwo": [],
            "Specjalizacja": [],
            "Priorytet": [],
            "Szpital": [],
            "Adres": [],
            "Dodatkowe Info": [],
            "Highlight": [],
            "Liczba Miejsc w trybie rezydenckim": [],
            "Liczba Miejsc w trybie pozarezydenckich": [],
            "Liczba Miejsc": [],
        }

    def add_specializations(self, name, specializations: typing.List[Specialization]):
        self.place_parser.set_data(name, specializations)
        for i in specializations:
            for j in i.places:
                self.add_field(
                    name,
                    i.name,
                    i.priority,
                    j.name,
                    j.address,
                    j.additional_info,
                    i.highlight,
                    j.availability,
                    i.resident_number,
                    i.non_resident_number,
                )

    def add_field(
        self,
        voivodeship,
        specialization,
        priority,
        hospital_name,
        address,
        additional_info,
        highlight,
        availability,
        resident_number,
        non_resident_number,
    ):
        self.data["Wojewodztwo"].append(voivodeship)
        self.data["Specjalizacja"].append(specialization)
        self.data["Priorytet"].append(priority)
        self.data["Szpital"].append(hospital_name)
        self.data["Adres"].append(address)
        self.data["Dodatkowe Info"].append(additional_info)
        self.data["Highlight"].append(highlight)
        self.data["Liczba Miejsc"].append(str(availability).replace(".0", ""))
        self.data["Liczba Miejsc w trybie rezydenckim"].append(
            str(resident_number).replace(".0", "")
        )
        self.data["Liczba Miejsc w trybie pozarezydenckich"].append(
            str(non_resident_number).replace(".0", "")
        )

    def save(self, output_directory: Path):
        output_path = "output.csv"
        if output_directory:
            output_path = output_directory / output_path
        df = pandas.DataFrame(self.data)
        df.to_csv(output_path, index=False)
