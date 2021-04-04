import numpy as np
import math

def bits_to_num(s, exp, sig):
    neg = int(s[0],2)
    if(int(s[1:1+exp],2)!=0):
        exponent = int(s[1:1+exp],2)-int('1'*(exp-1), 2)
        mantissa = int(s[1+exp:],2)*2**(-sig)+1
    else: #subnormal
        exponent = 1-int('1'*(exp-1), 2)
        mantissa = int(s[1+exp:],2)*2**(-sig)
    return ((-1)**neg)*(2**exponent)*mantissa