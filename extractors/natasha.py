from natasha import (
    NamesExtractor,
    SimpleNamesExtractor,
    PersonExtractor,

    LocationExtractor,
    AddressExtractor,

    OrganisationExtractor,

    DatesExtractor,

    MoneyExtractor,
    MoneyRateExtractor,
    MoneyRangeExtractor,
)

from natasha.markup import (
    show_markup_notebook as show_markup,
    format_json
)


class NatashaExtractor:

    def __init__(self, text):
        self.text = text

    def get_names(self):
        extractor = NamesExtractor()
        matches = extractor(self.text)
        facts = [_.fact.as_json for _ in matches]
        return facts

    def get_locations(self):
        extractor = LocationExtractor()
        matches = extractor(self.text)
        facts = [_.fact.as_json for _ in matches]
        return facts

    def get_addresses(self):
        extractor = AddressExtractor()
        matches = extractor(self.text)
        facts = [_.fact.as_json for _ in matches]
        return facts

    def get_dates(self):
        extractor = DatesExtractor()
        matches = extractor(self.text)
        facts = [_.fact.as_json for _ in matches]
        return facts

    def get_money(self):
        extractor = MoneyExtractor()
        matches = extractor(self.text)
        facts = [_.fact.normalized.as_json for _ in matches]
        return facts