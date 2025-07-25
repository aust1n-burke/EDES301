# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Simple Calculator (Refined)
--------------------------------------------------------------------------
License:   
Copyright 2025 - Austin Burke

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Now Python 2 and 3 compatible

Simple calculator that will 
  - Take in two numbers from the user
  - Take in an operator from the user
  - Perform the mathematical operation and provide the number to the user
  - Repeat

Operations:
  - addition
  - subtraction
  - multiplication
  - division
  - right shift
  - left shift
  - modulus
  - exponentiation

Error conditions:
  - Invalid operator --> Program should exit
  - Invalid number   --> Program should exit

--------------------------------------------------------------------------
"""

from __future__ import print_function
import operator
import sys

try:
    input = raw_input
except NameError:
    pass

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed for this example 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

operators = {
    "+"  : operator.add,
    "-"  : operator.sub,
    "*"  : operator.mul,
    "/"  : operator.truediv,
    ">>" : operator.rshift,
    "<<" : operator.lshift,
    "%"  : operator.mod,
    "**" : operator.pow
}

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def get_user_input():
    """Get input from the user.
         Returns tuple: (number, number, function) or 
         (None, None, None) if the inputs are invalid
    """
    try:
        # no longer immediately casts input numbers to floats
        number1 = input("Enter first number : ")
        number2 = input("Enter second number: ")
        op      = input("Enter function (valid values are +, -, *, /, >>, <<, %, **): ")
        
        # Support for int only operations:
        
        int_only = [">>", "<<", "%"]
        
        if (op in int_only): 
            
            if ((not number1.lstrip("-").isdigit()) or (not number2.rstrip("-").isdigit())): 
                print("This operand only works with integers!")
                return (None, None, None)
                
            number1 = int(number1)
            number2 = int(number2)

        else:
            number1 = float(number1)
            number2 = float(number2)
        
        func = operators.get(op)
            
    except:
        return (None, None, None)
    
    return (number1, number2, func)

# End def


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == "__main__":

    while True:
        (num1, num2, func) = get_user_input()
        
        if (num1 == None) or (num2 == None) or (func == None):
            print("Invalid input")
            break
        
        print(func(num1, num2))

