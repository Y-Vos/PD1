# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:12:23 2020

@author: naomi_000
"""

import numpy as np

numberSamples = 1000

confidenceIntervals = np.empty(0)     
means = np.empty(0)        
N = 10
numbGood = 0

while numberSamples > 0:
    sample =  np.random.normal(100, 10, N)
    std = np.std(sample, ddof=1)
    ste = std/(N**0.5)
    confidence = ste * 2.262
    confidenceIntervals = np.append(confidenceIntervals, confidence) 
    
    mean =  np.mean(sample)
    means = np.append(means, mean) 
    
    numberSamples = numberSamples - 1
    

for x in confidenceIntervals:
    y = float(means[np.where(confidenceIntervals == x)])
    maxInterval = y + x
    minInterval = y - x
    if maxInterval > 100 > minInterval:
        numbGood = numbGood + 1
        
print(f'{numbGood} of the 1000 had the mean in their confidence interval.')