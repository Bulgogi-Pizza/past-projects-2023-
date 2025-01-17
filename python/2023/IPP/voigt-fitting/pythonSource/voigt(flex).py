import numpy as np
from scipy import special

def voigt(v = None,par0 = None): 
    # vf= voigt(v,par0)
# input  --v: wavenumber
#        --par0: initial parameters. 4 by g matrix,first row is peak
#                position, second row is intensity,third row is Gaussain width,
#                fourth row is Lorentzian width
    
    # output -- vf: voigt
    
    v0 = par0[0]
    s = par0[1]
    ag = par0[2]
    al = par0[3]
    aD = (np.ones((len(v),1)) * ag)
#    if par0.ndim == 1:
#        vv0 = v * np.ones((1,1)) - np.ones((len(v),1)) * v0
#    else:
#        vv0 = v * np.ones((1,len(v0))) - np.ones((len(v),1)) * v0
    vv0 = v * np.ones((1,1)) - np.ones((len(v),1)) * v0
    
    vv0 = vv0[0]
    x = np.multiply(vv0,(np.sqrt(np.log(2)))) / aD
    x = x[0]
    y = np.ones((len(v),1)) * (al / ag) * (np.sqrt(np.log(2)))
    
    z = x + 1j * y
    z = z[0]
    w = special.wofz(z)
    
    #print(locals())
    
    #                      # University, Canada, March 2015.
    vf = w.real * np.transpose(s)
    return vf.real