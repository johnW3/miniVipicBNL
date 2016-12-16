import epics
from epics import PV
from epics import caget, caput, cainfo
from epics import ca
from epics import *
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

def findAvgPeak (list):
  sum = 0
  for ii in range (0, list.value.size):
    sum += ii * list.value[ii]
  return (sum / np.sum(list.value))

# finds dacTrim value where peak is in in waveform element 100
# 

def findBestDacTrim_V2 (pixel):
  desiredPeak = 100;
  wf = PV('vipic:Waveform1')
  caput('vipic:PixelToScan1',pixel)
  configCntWord = 1984
  configCntWordReg = PV('vipic:configPixelCnt1')
  configCntWordReg.put(configCntWord,wait=True)
  peak = findAvgPeak(wf)
  peakb = peak

  deltaFromDesired = abs(desiredPeak-peak)
  bestTrimDelta = abs(desiredPeak-peak)
  bestConfig = configCntWord
  delta1 = delta2 = 0
  print 'configCntWord = ', configCntWord, ' Peak = ', peak

  # if peak is within 1 of the desired peak then were done
  if ( deltaFromDesired > 1 ):
     if (peak > desiredPeak): 
         delta = -1 
     else:
         delta = 1
     configCntWord += delta
     configCntWordReg.put(configCntWord,wait=True)
     peak = findAvgPeak(wf)

     deltaFromDesired = abs(desiredPeak-peak)

     if (deltaFromDesired <= bestTrimDelta):
	bestTrimDelta = abs(desiredPeak-peak)
        bestConfig = configCntWord

     if ( deltaFromDesired > 1 ):
        # try to jump to correct config word
        deltaBetweenPeaks = abs(peakb - peak)
        deltaToPeak = abs(100-peak) 
        stepsToMove = floor( deltaToPeak / deltaBetweenPeaks )
	if (peak > desiredPeak):
		configCntWord -= stepsToMove;
	else:
		configCntWord += stepsToMove;

	while ( abs(desiredPeak-peak) > 1 ):
	    if (peak > desiredPeak):
			delta = -1
	    else:
			delta = 1
	    configCntWord += delta; 
	    configCntWordReg.put(configCntWord,wait=True)
	    peak = findAvgPeak(wf)
	    print 'configCntWord = ', configCntWord, ' Peak = ', peak, ' Delta = ', delta, delta1, delta2
	    if (abs(desiredPeak-peak) <= bestTrimDelta):
		bestTrimDelta = abs(desiredPeak-peak)
		bestConfig = configCntWord
	    if ( ( (delta == -1) and (delta1 == 1) and (delta2 == -1) ) or  ( (delta == 1) and (delta1 == -1) and (delta2 == 1) ) ):
		break
	    delta2 = delta1
	    delta1 = delta
  return bestConfig

def findBestDacTrim (pixel):
  wf = PV('vipic:Waveform1')
  caput('vipic:PixelToScan1',pixel)
  configCntWord = 1984
  configCntWordReg = PV('vipic:configPixelCnt1')
  configCntWordReg.put(configCntWord,wait=True)
  peak = findAvgPeak(wf)
  bestDelta = 100
  bestConfig = 1984
  delta = delta1 = delta2 = 0
  print 'configCntWord = ', configCntWord, ' Peak = ', peak
  while ( abs(100-peak) > 1 ):
    if (peak > 100):
	if ( (abs(100-peak) > 40) and (abs(delta) != 1) ) :
		delta = -5
	else:
        	delta = -1
    else:
	if ( (abs(100-peak) > 40) and (abs(delta) != 1) ):
		delta = 5
	else:
        	delta = 1
    configCntWord += delta; 
    configCntWordReg.put(configCntWord,wait=True)
    peak = findAvgPeak(wf)
    print 'configCntWord = ', configCntWord, ' Peak = ', peak, ' Delta = ', delta, delta1, delta2
    if (abs(100-peak) <= bestDelta):
	bestDelta = abs(100-peak)
        bestConfig = configCntWord
    if ( ( (delta == -1) and (delta1 == 1) and (delta2 == -1) ) or  ( (delta == 1) and (delta1 == -1) and (delta2 == 1) ) ):
	break
    delta2 = delta1
    delta1 = delta
  return bestConfig

# faster scan as of 12-08-2016
def scanAllPixels():
    bestDacTrim = np.zeros(1023)
    for ii in range(0, 1023):
        bestDacTrim[ii] = findBestDacTrim(ii)
	print 'Pixel ', ii, "  ", bestDacTrim[ii]
    print bestDacTrim
    return bestDacTrim

def scanAllPixels_ver2():
    bestDacTrim = np.zeros(1023)
    for ii in range(0, 1023):
        bestDacTrim[ii] = findBestDacTrim_V2(ii)
	print 'Pixel ', ii, "bestDacTrim = ", bestDacTrim[ii]
    print bestDacTrim
    return bestDacTrim

