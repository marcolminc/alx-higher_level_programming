#!/usr/bin/python3
"""Locked out class - prevention of dynamic instance attr creation.

This module creates a locked out class that prevents creation of
dynamic instance attributes except the one called first_name.
"""


class LockedClass:
    """An empty class locked out of dynamic instance attributes."""

    __slots__ = ['first_name']
