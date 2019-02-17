import re

class RegexExtractor:
    '''This class used standard python library for regular expression and search entities by rules.

    https://docs.python.org/3/library/re.html
    '''

    def __init__(self, text):
        self.text = text

    def get_names(self):
        return []

    def get_locations(self):
        return []

    def get_addresses(self):
        return []

    def get_dates(self):
        return []

    def get_money(self):
        return []