#!/usr/bin/env python3

class Item:
    """Handle all things items"""

    def __init__(self, name, desc):
        """Initialize an item, requiring a name and a description"""
        self.name = name
        self.desc = desc

    def add_to_level(self, level):
        """Add the item to a level"""
        level.add_item(self)

    def add_to_inventory(self):
        """Add the item to the inventory"""
        pass

    def rm_from_inventory(self):
        """Remove the item from the inventory"""
        pass

    def use(self):
        """Use the item if possible"""
        pass

    def use_with(self, item):
        """Use the item with another item, if possible"""
        pass

