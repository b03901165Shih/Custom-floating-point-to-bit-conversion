import numpy as np
import math

def float_to_bits(num, exp_b, sig_b):
    sign = ('1' if num<0 else '0')
    num = abs(num)
    bias = (2**(exp_b-1)-1)
    e = (0 if num==0 else math.floor(math.log(num,2)+bias))
    if(e>(2**(exp_b)-2)):#overflow
        exponent = '1'*exp_b
        mantissa = '0'* sig_b
    else:
        if(e>0):#normal
            s = num/2**(e-bias)-1
            exponent = bin(e)[2:].zfill(exp_b)
        else:   #submoral
            s = num/2**(-bias+1)
            exponent = '0'*exp_b
        mantissa = bin(int(s*(2**sig_b)+0.5))[2:].zfill(sig_b)[:sig_b]
    return sign+exponent+mantissa