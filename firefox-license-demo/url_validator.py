# url_validator.py
# This file is a modified version of a utility from Mozilla Firefox
# Original source: https://hg.mozilla.org/mozilla-central/file/tip/toolkit/components/places/URLClassifier.cpp 
# Licensed under MPL-2.0: https://www.mozilla.org/en-US/MPL/2.0/ 

import re


def is_valid_url(url):
    """
    Fungsi untuk memvalidasi apakah string adalah URL yang valid.
    Simulasi berdasarkan pola URL parsing dari Firefox.
    """
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None