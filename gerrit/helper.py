"""
Helper
======
Helper functions
"""

import json


def decode_json(gerrit_response):
    """
    Strip Cross Site Script Inclusion prefix from
    gerrit API response and return it as an object
    """

    return json.loads(gerrit_response.lstrip(')]}\''))