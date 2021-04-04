
from float2bit import float_to_bits
from bit2float import bits_to_num
    
if __name__=="__main__":
    test_num = 3.14159265
    exp = 8
    sig = 23
    print("=============(EXP, SIG) = (%d, %d)(Single)==========="%(exp, sig))
    print("Original number: %.8f"%test_num)
    print("Float to bits:  ",float_to_bits(test_num, exp, sig))
    print("Bits to Float:  ",bits_to_num(float_to_bits(test_num, exp, sig), exp, sig))
    
    exp = 6
    sig = 17
    print("\n=============(EXP, SIG) = (%d, %d)(Custom)==========="%(exp, sig))
    print("Original number: %.8f"%test_num)
    print("Float to bits:  ",float_to_bits(test_num, exp, sig))
    print("Bits to Float:  ",bits_to_num(float_to_bits(test_num, exp, sig), exp, sig))
    
    exp = 5
    sig = 11
    print("\n=============(EXP, SIG) = (%d, %d)(Single)==========="%(exp, sig))
    print("Original number: %.8f"%test_num)
    print("Float to bits:  ",float_to_bits(test_num, exp, sig))
    print("Bits to Float:  ",bits_to_num(float_to_bits(test_num, exp, sig), exp, sig))
    
    exp = 4
    sig = 6
    print("\n=============(EXP, SIG) = (%d, %d)(Custom)==========="%(exp, sig))
    print("Original number: %.8f"%test_num)
    print("Float to bits:  ",float_to_bits(test_num, exp, sig))
    print("Bits to Float:  ",bits_to_num(float_to_bits(test_num, exp, sig), exp, sig))
    