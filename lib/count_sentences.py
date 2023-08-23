#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=None):
        self._value = None
        if value is not None:
            self.value = value
    
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    def get_value(self):
        return self._value
    
    value = property(get_value, set_value)
    
    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        if self._value is None:
            return 0
        sentences = re.split(r'[.!?]', self._value)
        return len([sentence for sentence in sentences if sentence.strip()])