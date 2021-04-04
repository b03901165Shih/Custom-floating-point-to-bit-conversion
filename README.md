# Custom-floating-point-to-bit-conversion
This directory contains python and C++ codes of floating-point to bit-string conversion and bit-string to floating-point conversion functions.


## Usage (Python)

Number to bit-string in the specified exponent bit and fractional bit floating-point format:
```
>> float_to_bits(num, exp, sig)
```

Bit-string to number:
```
>> bits_to_num(string, exp, sig)
```

Example of running main.py:
```
=============(EXP, SIG) = (8, 23)(Single)===========
Original number: 3.14159265
Float to bits:   01000000010010010000111111011011
Bits to Float:   3.1415927410125732

=============(EXP, SIG) = (6, 17)(Custom)===========
Original number: 3.14159265
Float to bits:   010000010010010000111111
Bits to Float:   3.1415863037109375

=============(EXP, SIG) = (5, 11)(Single)===========
Original number: 3.14159265
Float to bits:   01000010010010001
Bits to Float:   3.1416015625

=============(EXP, SIG) = (4, 6)(Custom)===========
Original number: 3.14159265
Float to bits:   01000100101
Bits to Float:   3.15625
```
