#!/usr/bin/env python3

class Player:
    """The basic player class"""

    def __init__(self):
        """Initialize an empty inventory"""
        self.inventory = []

    def set_flag(self, **kwargs):
        """Set arbitrary (global) flags to mark progress"""
        self.__dict__.update(kwargs)

