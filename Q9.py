# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 04:26:38 2020

@author: Owais Raza
"""
#Create an empty string and assign it to the variable lett. Then using range, 
#write code such that when your code is run, lett has 7 b’s ("bbbbbbb").



lett = str("")

for i in range(7):
    lett += "b"
    
print(lett)