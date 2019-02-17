class DeepmiptExtractor:
    '''This class used pre-trained CNN model for Russian Named Entity Recognition.

    https://github.com/deepmipt/ner
    '''
    def __init__(self, text):
        self.text = text

    def get_names(self):
        return []

    def get_locations(self):
        return []