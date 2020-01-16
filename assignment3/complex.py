#!/usr/bin/env python3
from math import sqrt

class Complex:
    
    def __init__(self, real, imag):
        """Class for Complex numbers.
        
        args:
            real (int): the real part.
            imag (int): the imaginary part.

        """
        self.real = real
        self.imag = imag
        

    #Assignment 3.3

    def conjugate(self):
        """Calculates the conjugate of the complex number. Converts the sign of 
        the imaginary part to the opposite.

        Args:
            self (Complex(a, b)): complex number

        Return:
            Complex(a, -bi) or Complex(a, bi)

        """
        return Complex(self.real, self.imag*-1)
    
    def modulus(self):
        """Calculates the modulus of the complex number. Takes the squareroot
        of the two parts, real and imag, powered by 2 added together.

        Args:
            self (Complex(a, b)): complex number

        Return:
            sqrt(a^2 + b^2)

        """
        a = self.real**2
        b = self.imag**2
        return sqrt(a + b)
    
    def __add__(self, other):
        """Adds a complex number with another complex number(or with a simple
        integer). 

        Args:
            self (Complex(a, b), int): complex number or integer
            other (Complex(a, b)): complex number

        Return:
            Complex(a1 + a2, b1 + b2)

        """
        if isinstance(self, int):
            return Complex(other.real + self, other.imag)
        else:
            return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Subs a complex number with another complex number(or with a simple
        integer). 

        Args:
            self (Complex(a, b), int): complex number or integer
            other (Complex(a, b)): complex number

        Return:
            Complex(a1 - a2, b1 - b2)

        """
        if isinstance(self, int):
            return Complex(other.real - self, other.imag)
        else:
            return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """Multiplicate a complex number with another complex number(or with a 
        simple integer). 

        Args:
            self (Complex(a, b), int): complex number or integer
            other (Complex(a, b)): complex number

        Return:
            Complex(a1 * a2 − b1 * b2, a1 * b2 + a2 * b1)

        """
        return Complex((self.real * other.real) - 
        (self.imag * other.imag), 
        ((self.real * other.imag) + 
        (self.imag * other.real)))
    
    def __eq__(self, other):
        """Check if two complex numbers are equal. 

        Args:
            self (Complex(a, b)): complex number
            other (Complex(a, b)): complex number

        Return:
            True: if they are equal
            false: if they are different

        """
        if((self.real == other.real) & (self.imag == other.imag)):
             return True
        return False
    

    #Assignment 3.4

    def __radd__(self, other):
        """Makes the addition between complex number and integer possible.

        Args:
            self (Complex(a, b), int): complex number or integer
            other (Complex(a, b)): complex number

        Return:
            call on __add__ function

        """
        return self + other

    def __rmul__(self, other):
        """Makes the multiplication between complex number and integer possible.

        Args:
            self (Complex(a, b), int): complex number or integer
            other (Complex(a, b)): complex number

        Return:
            call on __mul__ function

        """
        return other * self

    def __rsub__(self, other):
        """Makes the substraction between complex number and integer possible.

        Args:
            self (Complex(a, b), int): complex number or integer
            other (Complex(a, b)): complex number

        Return:
            call on __add__ function

        """
        return other - self
