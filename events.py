#!/usr/bin/env python3

class Event:
    def __init__(self, name, message=[], setflags=[], unsetflags=[],
                 toggleflags=[]):
        """Initialize an event with its name"""
        self.name = name
        self.message = message
        self.setflags = setflags
        self.unsetflags = unsetflags
        self.toggleflags = toggleflags

    def trigger(self):
        """Do what the event is configured to do"""
        if self.message:
            # TODO: pipe message to output
            pass
        for flag in self.setflags:
            flag = True
        for flag in self.unsetflags:
            flag = False
        for flag in self.toggleflags:
            flag = False if flag else True

