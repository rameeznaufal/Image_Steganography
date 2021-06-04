import cv2
import numpy as np
import types
from pyfiglet import Figlet

def messageToBinary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "08b") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")

def Steganography(): 
    print()
    f=Figlet(font='alligator2',justify='center',width=150)
    print(f.renderText('I m a g e'))
    print(f.renderText('Steganography'))
    a = input(" \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
    userinput = int(a)
    if (userinput == 1):
      print("\nEncoding....")
      #encode_text() 
    elif (userinput == 2):
      print("\nDecoding....") 
      print("Decoded message is "                ) 
                                  #+  decode_text() 
    else: 
      raise Exception("Enter correct input") 

if __name__ == "__main__":
    Steganography()        