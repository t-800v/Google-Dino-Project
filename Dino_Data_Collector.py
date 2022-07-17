# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 15:36:45 2022

@author: Ceyhun
"""
import keyboard
from mss import mss

def num_generator():
    
    for i in range(1000):
        
        yield(i)
        
generator1 = num_generator()

generator2 = num_generator()

ss_manager = mss()


while True:
    
    if keyboard.is_pressed(keyboard.KEY_UP):
        
        img = ss_manager.grab({"top":850, "left":230, "width":450, "height":220})
        image = Image.frombytes("RGB", img.size, img.rgb)
        
        num_0 = next(generator1)
        image.save(f"C://Users/Ceyhun/Desktop/Dino2/Up{num_0}.png")
        time.sleep(0.1)
        
    elif keyboard.is_pressed("right"):
         
        img = ss_manager.grab({"top":850, "left":230, "width":450, "height":220})
        image = Image.frombytes("RGB", img.size, img.rgb)
        
        num_1 = next(generator1)
        image.save(f"C://Users/Ceyhun/Desktop/Dino2/None{num_1}.png")
        time.sleep(0.1)
        
    
    elif keyboard.is_pressed("s"):
        
        break