import typing

import pandas

from specialization_filter.core.parser import Parser
from specialization_filter.core.specialization import Specialization


class PlaceParser(Parser):
    def get_name(self):
        return "places.csv"

    def get_delimiter(self) -> str:
        return ","

    def set_data(self, name, specializations: typing.List[Specialization]):
        voivodeship = None
        for _, row in self.data.iterrows():
            if pandas.isna(row["rezydent"]) and pandas.isna(row["pozarezydent"]):
                if row["specialization"].lower() == name.lower():
                    voivodeship = row["specialization"]
            if voivodeship == None:
                continue
            for i in specializations:
                if row["specialization"].lower() == i.name.lower():
                    i.resident_number = row["rezydent"]
                    i.non_resident_number = row["pozarezydent"]

    def run(self):
        last_specialization = None
        for _, row in self.data.iterrows():
            if pandas.isna(row["rezydent"]) and pandas.isna(row["pozarezydent"]):
                last_specialization = Specialization(row["specialization"])
            else:
                last_specialization.add_place(
                    row["place"], row["address"], row["availability"]
                )
        return self.specializations
