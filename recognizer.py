from extractors.natasha import NatashaExtractor
from validator import Validator


class Recognizer(object):
    '''Class Recognizer get text parameter and try to recognize entities like names, dates, locations, addresses and
    money
    '''

    def __init__(self, text):
        '''This method initialize parameters and create objects of several extractors type

        :param text: input text
        '''
        self.text = text
        self.validator = Validator()
        self.natashaExtractor = NatashaExtractor(self.text)

    @staticmethod
    def _remove_duplicated_names(name_list):
        separator = '@'

        # delete duplicated values
        result_set = set()
        for item in name_list:
            name = ""
            if 'first' in item:
                name = item['first']
            name += separator
            if 'middle' in item:
                name += item['middle']
            name += separator
            if 'last' in item:
                name += item['last']
            result_set.add(name)

        # convert set to list
        result_list = []
        for item in result_set:
            first, middle, last = item.split(separator)
            name_dict = {}
            name_dict['first'] = first
            name_dict['middle'] = middle
            name_dict['last'] = last
            result_list.append(name_dict)

        return result_list

    @staticmethod
    def _remove_duplicated_dates(date_list):
        return date_list

    @staticmethod
    def _remove_duplicated_location(location_list):
        result_set = set()
        for item in location_list:
            result_set.add(item['name'])

        result_list = list(result_set)
        return result_list

    @staticmethod
    def _remove_duplicated_addresses(address_list):
        return address_list

    @staticmethod
    def _remove_duplicated_money(money_list):
        return money_list

    def _get_names(self):
        '''Search names in text'''
        names_list = []
        names_list += self.natashaExtractor.get_names()

        cleared_list = Recognizer._remove_duplicated_names(names_list)
        result = self.validator.check(cleared_list, "name")
        return result

    def _get_dates(self):
        '''Search dates in text'''
        date_list = []
        date_list += self.natashaExtractor.get_dates()

        cleared_list = Recognizer._remove_duplicated_dates(date_list)
        result = self.validator.check(cleared_list, "date")
        return result

    def _get_locations(self):
        '''Search locations in text'''
        location_list = []
        location_list += self.natashaExtractor.get_locations()

        cleared_list = Recognizer._remove_duplicated_location(location_list)
        result = self.validator.check(cleared_list, "location")
        return result

    def _get_addresses(self):
        '''Search addresses in text'''
        address_list = []
        address_list += self.natashaExtractor.get_addresses()

        cleared_list = Recognizer._remove_duplicated_addresses(address_list)
        result = self.validator.check(cleared_list, "address")
        return result

    def _get_money(self):
        '''Search money in text'''
        money_list = []
        money_list += self.natashaExtractor.get_money()

        cleared_list = Recognizer._remove_duplicated_money(money_list)
        result = self.validator.check(cleared_list, "money")
        return result

    def get_entities(self, param=None):
        '''Search in text entities, which is contained in argument param. If param containes value "all" then
        method return all existed entities'''
        result = {}

        if 'name' in param or 'all' in param:
            result['name'] = self._get_names()
        if 'date' in param or 'all' in param:
            result['date'] = self._get_dates()
        if 'location' in param or 'all' in param:
            result['location'] = self._get_locations()
        if 'address' in param or 'all' in param:
            result['address'] = self._get_addresses()
        if 'money' in param or 'all' in param:
            result['money'] = self._get_money()

        return result
