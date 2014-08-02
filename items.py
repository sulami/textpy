#!/usr/bin/env python3

class Item:
    """Handle all things items"""

    def __init__(self, name, desc, usable=False, removeonuse=True,
                 useeffect=None, usablewith=[]):
        """Initialize an item"""
        self.name = name
        self.desc = desc
        self.usable = usable
        self.removeonuse = removeonuse
        self.useeffect = useeffect
        self.usablewith = usablewith

    def add_to_level(self, level):
        """Add the item to a level"""
        level.add_item(self)

    def add_to_inventory(self):
        """Add the item to the inventory"""
        player.inventory.append(self)

    def rm_from_inventory(self):
        """Remove the item from the inventory"""
        if self not in player.inventory:
            return
        player.inventory.remove(self)

    def use(self):
        """Use the item if possible"""
        if not self.usable:
            return
        if self.removeonuse:
            self.rm_from_inventory()
        self.useeffect()

    def use_with(self, item):
        """Use the item with another item, if possible"""
        if not self.usable or item not in self.usablewith:
            return
        self.useeffect()

