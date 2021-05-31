#!/usr/bin/python3
"""
In this module a single function that returns JSON of an object.
"""
import json


def to_json_string(my_obj):
	""" Returns the JSON representation of
	an object (string). Serializes.

	Args:
		my_obj (str): String to serialize.

	"""
	try:
		return json.dumps(my_obj)
	except TypeError:
		message = str(my_obj) + " is not JSON serializable"
		raise TypeError(message)
