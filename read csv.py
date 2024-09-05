# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv

with open('recipt.csv', 'r') as file:
    
    # call reader
    
    file_csv = csv.reader(file)
    
 #start reading and displaying rows
    
 #running total
    
    price_total = 0
    
 # to skip the header row
    
    next(file_csv)
    
    for row in file_csv:
        
        product, quant, price = row
        
        print(product, quant, price)
        
        price_total += float(price)
        
    print("Total Price: $", price_total, sep='')
        
        
        
        
        
        
        
        
        
        
        
        












