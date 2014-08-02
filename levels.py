#!/usr/bin/env python3

class Level:
    """Handle everything that makes up a level"""

    def __init__(self, desc):
        """Initialize level object, requiring the description"""
        self.desc = desc
        self.routes = {}
        self.items = []

    def open_level(self):
        """Return the level description"""
        # TODO: load up any events that may be present
        return self.desc

    def add_route(self, direction, target):
        """Add a single route pointing to a level to the level"""
        self.routes[direction] = target

    def rm_route(self, direction):
        """Remove a single route from the level"""
        if direction not in self.routes:
            return
        del self.routes[direction]

    def go_route(self, direction):
        """Go a route from the level, returning the new level"""
        if direction not in self.routes:
            return None
        return self.routes[direction]

    def add_item(self, item):
        """Add a single item to the level"""
        self.items.append(item)

    def take_item(self, item):
        """Take an item from the level and add it to the inventory"""
        if item not in self.items:
            return
        self.rm_item(item)
        item.add_to_inventory()

    def rm_item(self, item):
        """Remove a single item from the level"""
        if item not in self.items:
            return
        self.items.remove(item)

"""
HELPER FUNCTIONS
"""

def change_level(direction):
    if direction not in LEVEL.routes:
        return
    LEVEL = LEVEL.go_route(direction)
    return LEVEL.open_level()

