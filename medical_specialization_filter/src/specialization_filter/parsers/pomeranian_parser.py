import pandas

from specialization_filter.core.parser import Parser
from specialization_filter.core.specialization import Specialization


class PomeranianParser(Parser):
    def get_name(self):
        return "pomorze.csv"

    def run(self):
        last_specialization = None
        for _, row in self.data.iterrows():
            if pandas.isna(row["availability"]) and pandas.isna(row["address"]):
                if row["place"] == "Brak":
                    continue
                if last_specialization is not None:
                    self.specializations.append(last_specialization)
                last_specialization = Specialization(row["place"])
            else:
                last_specialization.add_place(
                    row["place"], row["address"], row["availability"]
                )
        self.specializations.append(last_specialization)
        return self.specializations
