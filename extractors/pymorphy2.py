class Pymorphy2Extractor:
    '''This class used pymorphy2 library and it class MorphAnalyzer to search names from text

    https://github.com/kmike/pymorphy2
    '''

    def __init__(self, text):
        self.text = text

    def get_names(self):
        return []