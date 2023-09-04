import typing

from specialization_filter.config.configuration import Configuration


class SpecializationPlace:
    def __init__(self, name, address, availability):
        self.name = name
        self.address = address
        self.availability = availability
        self.additional_info = Configuration.get_additional_address_info(address)


class Specialization:
    def __init__(self, name):
        name = name.replace("\n", " ").replace("\r", "").replace("  ", " ")
        self.name = name
        self.priority = self.set_priority(name)
        self.highlight = self.set_main_recommendations(name)
        self.places: typing.List[SpecializationPlace] = []
        self.resident_number = 0
        self.non_resident_number = 0

    def add_place(self, name, address, availability):
        self.places.append(SpecializationPlace(name, address, availability))

    def set_main_recommendations(self, name):
        recommendations = Configuration.get_recommended_specializations()
        blacklist = Configuration.get_blacklist_specializations()
        for i in blacklist:
            if i in name.lower():
                return False
        for i in recommendations:
            if i in name.lower():
                return True
        return False

    def set_priority(self, name: str):
        if name.lower() in Configuration.get_priority_specializations():
            return True
        return False
