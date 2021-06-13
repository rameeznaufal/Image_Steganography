import cv2
import os
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

def hideData(image, secret_message):
  n_bytes = image.shape[0] * image.shape[1] * 3 // 8
  print("Maximum bytes to encode:", n_bytes)
  if len(secret_message) > n_bytes:
      raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")
  
  secret_message += "#####" #  delimeter

  data_index = 0
  binary_secret_msg = messageToBinary(secret_message)
  data_len = len(binary_secret_msg)
  for values in image:
      for pixel in values:
          r, g, b = messageToBinary(pixel)
          
          if data_index < data_len:
              pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index < data_len:
              pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index < data_len:
              pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index >= data_len:
              break
      if data_index >= data_len:
              break
  return image

def encode_text(): 
  image_name = input("Enter image name (with extension): ") 
  image = cv2.imread(image_name) 
  
  print("The shape of the image is: ",image.shape) 
  print("The original image is as shown below: ")
  resized_image = cv2.resize(image, (500, 500))
  cv2.imshow(resized_image) 
    
  data = input("Enter data to be encoded : ") 
  if (len(data) == 0): 
    raise ValueError('Data is empty')
  
  filename = input("Enter the name of new encoded image(with extension): ")
  encoded_image = hideData(image, data) 
  cv2.imwrite(filename, encoded_image)

def Steganography(): 
    while True: 
      print()
      f=Figlet(font='alligator2',justify='center',width=150)
      print(f.renderText('I m a g e'))
      print(f.renderText('Steganography'))
      a = input(" \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
      try:
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
      except:
         print('\n !!! ENTER THE CORRECT OPTION !!! \n ')    
      finally:
         ch = str(input(" Do you want to go back ? (Y/n)")).upper()
      os.system('cls')
      if ch!='Y':
          break

if __name__ == "__main__":
    Steganography()        