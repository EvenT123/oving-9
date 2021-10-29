# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 12:13:35 2021

@author: Bruker
"""

with open("sporsmaalsfil.txt", "r", encoding="UTF-8") as file:
    List = []
    for line in file:
        if line.find(":"):
            spm = line.split(":")
            List.append(spm[0])
            alt = spm[-1]
            List.append(alt)
            cor = spm[1]
            List.append(cor)

    print(List)