#!/usr/bin/env python
import yaml

class Dictionary():

    def __init__(self):
        with open("Dictionary", 'r') as stream:
            try:
                data_loaded = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.spanish_words = data_loaded['spanish_words']
        self.english_words = data_loaded['english_words']

