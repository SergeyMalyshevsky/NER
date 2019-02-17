class Validator(object):

    def __init__(self):
        pass

    def _check_names(self, data):
        '''Check names for correct value by dictionary and remove incorrect values'''

        # TODO check names
        return data

    def _check_dates(self, data):
        '''Check dates for correct value by dictionary and remove incorrect values'''

        # TODO check dates
        return data

    def _check_locations(self, data):
        '''Check locations for correct value by dictionary and remove incorrect values'''

        # TODO check locations
        return data

    def _check_addresses(self, data):
        '''Check addresses for correct value by dictionary and remove incorrect values'''

        # TODO check addresses
        return data

    def _check_money(self, data):
        '''Check money list for correct value by dictionary and remove incorrect values'''

        # TODO check money
        return data

    def check(self, data, type):
        if type == "name":
            return self._check_names(data)
        elif type == "date":
            return self._check_dates(data)
        elif type == "location":
            return self._check_locations(data)
        elif type == "address":
            return self._check_addresses(data)
        elif type == "money":
            return self._check_money(data)
