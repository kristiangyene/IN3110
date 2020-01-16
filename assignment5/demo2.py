import re
import sys
from demo import Dog

#Simple class in python
class Dog:       

    def __init__(self, name, yrs):
        self._name = name    
        self._tagged = True
        self._friends = []
        self._years = yrs
    """See if 
    
    a friend exist"""
    def print_friend(self, dog):
        for friend in self._friends:
            if friend == dog:
                print(self._name + " and " + friend + " are friends.")
                return
        print("Could not find friend")
