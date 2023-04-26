# import library
import numpy as np
import pywt
from peak_det import peakdet
import matplotlib.pyplot as plt

# Calculatae fault location 
# input : voltage from three phase  
def fault_location(Va,Vb,Vc):
    
    # Clarke transformation for getting base voltage
    V1=np.multiply(Va,0.57735)+ np.multiply(Vb,0.57735) + np.multiply(Vc,0.57735)
    V2=np.multiply(Va,0.81645)+ np.multiply(Vb,-0.40825) + np.multiply(Vc,-0.40825)
    V3=np.multiply(Vb,0.70711) + np.multiply(Vc,-0.70711)
	
    # Wavelet db4 transformation to produce detailed coefficient and approximation coefficient
	#for ground and aerial mode

    [ca1,cd1] = pywt.dwt(V1, 'db4')
    [ca2,cd2] = pywt.dwt(V2, 'db4')
	
	# convert cd2 coefficient to abs value

    cd2abs=abs(cd2)
    plt.figure().set_figwidth(20)
    plt.plot(cd2abs[4000:7500])
    #plt.show()
    
    plt.savefig('wavelet.png', bbox_inches='tight', facecolor='w')
    
    [maxi,mini]=peakdet(cd2abs,10)
    t1=maxi[0][0]
    t2=maxi[1][0]
    t3=maxi[2][0]
    f=t2-t1
	
    if f==1 or f==2 :
        deltat=t3-t1
    else:
        deltat=f
    
    # calculate fault location
    L=len(cd2abs)
    V=297074.826
    position_=(V*deltat*0.5/L)/2


    return position_