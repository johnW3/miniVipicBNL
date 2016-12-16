import epics
from epics import PV
import time
import array

from math import *
from string import *
import time
import copy
import os
import sys
#os.environ['EPIC

import numpy as np
import matplotlib.pyplot as plt

P="vipic:"
H="zyw:"

def findAvgPeak (list):
  sum = 0
  for ii in range (0, list.value.size):
    sum += ii * list[ii]
  return (sum / np.sum(list.value))



aCalcRecord = "xxx:userArrayCalc10"
calc = aCalcRecord + ".CALC"
result = aCalcRecord + ".VAL"
aresult = aCalcRecord + ".AVAL"


#waveform = epics.caget('vipic:Waveform1')
wf1 = PV('vipic:Waveform1')

wf2 = numpy.array
wf2 = PV('vipic:Waveform1')

dacTrim = PV('vipic:dacTrim1')

configWordCnt = PV('vipic:configPixelCnt1')

#plt.plot(wf2.value)
#plt.show()

max_index = np.nanargmax(wf2.value)
flat_avg = np.average(np.flatnonzero(wf2.value))

sum = 0
for ii in range(0, wf2.value.size):
    sum += ii * wf2.value[ii]

weighted_index_avg = sum / np.sum(wf2.value)
print weighted_index_avg

# dac trims lowest = 1920 to highest = 
for ii in range(1920, )
    


