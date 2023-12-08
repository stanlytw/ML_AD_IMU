# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:03:28 2023

@author: stanly-lin
"""
import numpy as np 
import pandas as pd
import os
import math
### get data for MCU inference test latter, and this data will not be train.  
def remove_emptyline_symbol(pth, symbol):
    
    file_list = []
    for file in os.listdir(pth):
        file_list.append(os.path.join(pth, file))
    file_list.sort()

    print(file_list)
    #return _df, _df_test
# Python program to
# demonstrate reading files
# using for loop

L = ["Geeks\n", "for\n", "Geeks\n"]

#remove_emptyline_symbol('data/wing', "a") 

# Opening to file
file1 = open('data/negative/output_negative_1.txt', 'r')
file2 = open('data/negative/ad_output_negative_1.txt', 'w')
count = 0
 
# Using for loop
print("Using for loop")
for line in file1:
    count += 1
    #print("Line{}: {}".format(count, line[0]))
    #file2.writelines(line)
    if((line[0]=="-") and (line[1]==",")):
        print("Dummy Line{}: {}".format(count, line.strip()))
    elif((line[0]=="\n")):
        print("Empty Line{}: {}".format(count, line.strip()))
    else:
        file2.writelines(line)    
# Closing files
file1.close()
file2.close()