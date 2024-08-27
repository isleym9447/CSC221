# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:16:58 2024

@author: isbla
"""


def main():
    numStu = int(input("Please enter how many students you would like to add: "))
    names,scores = getStuInfo(numStu)
    dis_Stu_Info(names, scores)
    
    
def getStuInfo(numStu):
    
    names = []
    scores = []
    
    
    
    for i in  range(1, numStu+1):
        
        name = input("Please enter a name ")
        names.append(name)
        score = input("Please enter a score ")
        scores.append(score)
        
        
        
    return names, scores

def dis_Stu_Info(names, sscores):
    print(f"{'Name':<10} {'Score'}")
    print('-'*20)
    for i in range(len(names)): 
        
        print(f"{names[i]:<10}{scores[i]}")
 
main()
    