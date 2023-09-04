import typing

from specialization_filter.core.parser import Parser
from specialization_filter.core.specialization import Specialization


class MasovianParser(Parser):
    def get_name(self) -> str:
        return "mazowieckie.csv"

    def run(self):
        specializations: typing.Dict[str, Specialization] = {}
        for _, row in self.data.iterrows():
            if row["specialization"] not in specializations:
                specializations[row["specialization"]] = Specialization(
                    row["specialization"]
                )
            specializations[row["specialization"]].add_place(
                row["upper_place"] + " - " + row["place"],
                row["address"],
                row["availability"],
            )
        for k, v in specializations.items():
            self.specializations.append(v)
        return self.specializations
