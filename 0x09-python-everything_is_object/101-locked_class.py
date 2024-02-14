#!/usr/bin/python3
"""
Define a locked class
"""

class LockedClass:
	"""
	LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes,
	except if the new instance attribute is called first_name.
	"""
	__slot__ = "first_name"
