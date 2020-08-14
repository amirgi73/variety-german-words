#!/usr/bin/python
### BEGIN LICENSE
# Copyright (c) 2020, amirgi73
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END OF LICENSE

"""
    A quotes plugin to show German words with translation and examples.
    A helpful way to get better at German
    
    This script is placed in '~/.config/variety/plugins' and then activated
    from inside Variety's  Preferences Quotes menu
"""

import logging
import random
from locale import gettext as _
from csv import reader
from variety.Util import Util
from variety.plugins.IQuoteSource import IQuoteSource
import os

logger = logging.getLogger("variety")

german_words_file = os.path.expanduser('~/.config/variety/plugins/variety-german-words/words.csv')


class GermanWordsSource(IQuoteSource):
    """
        Retriving words and their translations from words.csv file
        Attributes:
            quotes(list): list containing the quotes
    """

    def __init__(self):
        self.active = False
        super(IQuoteSource, self).__init__()
        self.quotes = []

    @classmethod
    def get_info(cls):
        return {
            "name": "German Words",
            "description": _("Showing German words and their meaning as a way to learn German\n"
                             "Does not support searching by tags or authors."),
            "author": "amirgi73",
            "url": "https://github.com/amirgi73/variety-german-words",
            "version": "0.0.1"
        }

    def supports_search(self):
        return False

    def activate(self):
        if self.active:
            return
        self.active = True
        self.quotes = []
        self.fetch_german_words()

    def deactivate(self):
        self.quotes = []
        self.active = False

    # def is_active(self):
    #    return self.active

    def fetch_german_words(self):
        self.quotes = []
        # TODO: read the german_words.csv and return them
        with open(german_words_file, 'r') as fin:
            file_reader = reader(fin)
            words_from_file = []
            for row in file_reader:
                data = {
                    'English': row[1],
                    'Persian G-translate': row[2],
                    'Persian B-amooz': row[3],
                    'German': row[5],
                    'German Alternatives': row[6],
                    'Level': row[7],
                    'Part of Speech': row[8],
                    'Plural and Inflected Forms': row[10],
                    'Sample Sentence': row[11],
                }
                words_from_file.append(data)

        for item in words_from_file:
            if item.get('Plural and Inflected Forms'):
                source_name = f"\tPlural/Inflected Forms: {item.get('Plural and Inflected Forms')}"
            else:
                source_name = ''
            self.quotes.append({
                "quote": f"{item.get('German')} : {item.get('English')}\n{item.get('Sample Sentence')}\n",
                "author": item.get('Part of Speech'),
                "sourceName": source_name})

        if not self.quotes:
            logger.warning("Could not read words ")

    def get_for_author(self, author):
        return []

    def get_for_keyword(self, keyword):
        return []

    def get_random(self):
        return self.quotes
