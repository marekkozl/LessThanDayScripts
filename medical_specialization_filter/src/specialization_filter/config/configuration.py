import typing


class Configuration:
    @staticmethod
    def get_additional_address_info(address: str) -> str:
        address_lower = address.lower()
        if (
            "gdańsk" in address_lower
            or "gdynia" in address_lower
            or "sopot" in address_lower
        ) and "starogard" not in address_lower:
            additional_info = "Trójmiasto"
        elif "warszawa" in address_lower:
            additional_info = "Warszawa"
        elif "katowice" in address_lower:
            additional_info = "Katowice"
        elif "wrocław" in address_lower:
            additional_info = "Wrocław"
        else:
            additional_info = "Zadupie"
        return additional_info

    @staticmethod
    def get_recommended_specializations() -> typing.List[str]:
        return ["aneste", "reumat", "neuro", "endokry", "onkolo", "hemato"]

    @staticmethod
    def get_blacklist_specializations() -> typing.List[str]:
        return [
            "radioterapia",
            "dziecięca",
            "chirurgia",
            "ginekolog",
            "neuropatologia",
        ]

    @staticmethod
    def get_priority_specializations() -> typing.List[str]:
        return [
            "anestezjologia",
            "intensywna terapia",
            "chirurgia dziecięca",
            "chirurgia ogólna",
            "chirurgia onkologiczna",
            "choroby wewnętrzne",
            "choroby zakaźne",
            "geriatria",
            "hematologia",
            "kardiologia dziecięca",
            "medycyna paliatywna",
            "medycyna ratunkowa",
            "medycyna rodzinna",
            "neonatologia",
            "neurologia",
            "neurologia dziecięca",
            "onkologia i hematologia dziecięca",
            "onkologia kliniczna",
            "patomorfologia",
            "pediatria",
            "psychiatria",
            "psychiatria dzieci i młodzieży",
            "radioterapia onkologiczna",
            "stomatologia dziecięc",
        ]
