from numpy import mean, sqrt, square, arange
import sys
import os



def rms_check(Va,Vb,Vc):
    #   Normal RMS voltage from simulation  
    Varmsn = 337008
    Vbrmsn = 338237.4
    Vcrmsn = 336890.7
 
    #   Calculate VRMS all phase
    Varms = sqrt(mean((Va**2)))
    Vbrms = sqrt(mean((Vb**2)))
    Vcrms = sqrt(mean((Vc**2)))
 
    #   scale for voltage minimal 
    k=0.863022517
 
    #   minimal normal voltage for all phase
    Vamin=Varmsn*k
    Vbmin=Vbrmsn*k
    Vcmin=Vcrmsn*k


    if (Varms <= Vamin):
        Vaf=1
    else :
        Vaf=0   
    if (Vbrms <= Vbmin): 
        Vbf=1
    else :
        Vbf=0
    if (Vcrms <= Vbmin): 
        Vcf=1
    else :
        Vcf=0
        
    
    
    return Vaf,Vbf,Vcf,Varms,Vbrms,Vcrms