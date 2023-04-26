from csv import reader
from numpy import mean, sqrt, square, arange
import numpy as np
import pywt
import time
import csv
from peak_det import peakdet
from rms_check import rms_check
from calculate_location import fault_location
import sys
import os
from time import sleep





with open('50.csv', 'r') as f:
    data = list(reader(f))
	
	
#   store data to array
t = [i[0] for i in data[1::]]
Va = [i[1] for i in data[1::]]
Vb = [i[2] for i in data[1::]]
Vc = [i[3] for i in data[1::]]

Va=np.array(Va,dtype=float)
Vb=np.array(Vb,dtype=float)
Vc=np.array(Vc,dtype=float)

[Vaf,Vbf,Vcf,Varms,Vbrms,Vcrms]=rms_check(Va,Vb,Vc)
Varmst=str(Varms)
Vbrmst=str(Vbrms)
Vcrmst=str(Vcrms)
if (Vaf==1):
    Vateks='Fault'
else:
     Vateks='Normal'
if (Vbf==1):
    Vbteks='Fault'
else:
    Vbteks='Normal'
if (Vcf==1):
    Vcteks='Fault'
else:
    Vcteks='Normal'
    
if (Vaf==1) or (Vbf==1) or (Vcf==1):
    position=fault_location(Va,Vb,Vc)
    position_=str(position)
    print(position)
else:
    print('Normal')
    posisis='Normal'
