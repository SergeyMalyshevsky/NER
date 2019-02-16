from extractors.natasha import NatashaExtractor

class Recognizer(object):

    def __init__(self, text):
        self.text = text
        self.natashaExtractor = NatashaExtractor(self.text)


    def _get_names(self):
        natasha_result = self.natashaExtractor.get_names()
        separator = '@'

        # delete duplicated values
        result_set = set()
        for item in natasha_result:
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


    def _get_dates(self):
        result = self.natashaExtractor.get_dates()
        return result


    def _get_locations(self):
        natasha_result = self.natashaExtractor.get_locations()
        result_set = set()
        for item in natasha_result:
            result_set.add(item['name'])

        result_list = list(result_set)
        return result_list


    def _get_addresses(self):
        result = self.natashaExtractor.get_addresses()
        return result


    def _get_money(self):
        result = self.natashaExtractor.get_money()
        return result


    def get_entities(self, param=None):
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