#include <iostream>
#include <cstdlib>
#include <cmath>
#include <bitset>
#include <string>
#include <bits/stdc++.h>

constexpr int exp_b = 7;
constexpr int sig_b = 22;
constexpr int num_b = 1+exp_b+sig_b;

//change f into integer expression of bit strings (custom floating point)
int double_to_bitint(double f)
{
    int sign = (f<0)?-1:1;
    f = abs(f);
    double bias = pow(2,(exp_b-1))-1; 
    double s;
    int e = (f==0)?0:int(floor((log(f)/log(2))+bias));
    string expo, mant;
    if(e>(pow(2,exp_b)-2))  {
        expo = bitset<exp_b>(int(pow(2, exp_b)-1)).to_string();
        mant = bitset<sig_b>(0).to_string();
    }
    else{
        if(e>0){
            s = f/(pow(2,e-bias))-1;
            expo = bitset<exp_b>(e).to_string();
        }
        else{
            s = f/(pow(2,1-bias));
            expo = bitset<exp_b>(0).to_string();
        }
        mant = bitset<sig_b>(int(s*pow(2, sig_b)+0.5)).to_string();
    }
    int trans_num = stoi("0"+expo+mant, nullptr, 2);
    trans_num = (sign==-1)?(trans_num | (1UL << (num_b-1))):trans_num;
    return trans_num;
}