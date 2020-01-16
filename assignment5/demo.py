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
    ''' single  multiline'''
    def print_friend(self, dog):
        for friend in self._friends:
            if friend == dog:
                print(self._name + " and " + friend + " are friends.")
                return
        print("Could not find friend")

    def get_name(self):
        return self._name

    def set_friend(self, dog):
        self._friends.append(dog)

    @Override
    def checkYrs(self):
        if self._years > 5:
            print(self._name + " is a senior.")
        elif self._years < 1:
            print(self.name + " is a puppy.")
        else:
            print(self._name + " is a junior.")
    
    def addYr(self, yrs):
        while yrs != 10:
            yrs+= 1
    
    def readFile(self, filename):
        try:
            dog_file = open(filename, "r") 
            for line in dog_file.readlines():
                name, breed = line.split(" ")
                print(name, " ", breed)

        except IOError as error:
            print("Cannot open file: " + filename)
            sys.exit(0)
            
        
d = Dog("Fido", 4)
e = Dog("Buddy", 6)
print(e.get_name)
e.set_friend(d.get_name)
e.print_friend("Fido")
