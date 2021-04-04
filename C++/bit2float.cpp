#include <iostream>
#include <cstdlib>
#include <cmath>
#include <bitset>
#include <string>
#include <bits/stdc++.h>

constexpr int exp_b = 7;
constexpr int sig_b = 22;
constexpr int num_b = 1+exp_b+sig_b;

float bitint_to_float(int bits)
{
    string s = bitset<num_b>(bits).to_string();
    float expo, mant;
    if(stoi(s.substr(1,exp_b), nullptr, 2)!=0)
    {
        expo = stoi(s.substr(1,exp_b), nullptr, 2)-(pow(2,exp_b-1)-1);
        mant = float(stoi(s.substr(1+exp_b,sig_b), nullptr, 2))*pow(2, -sig_b)+1;
    }
    else //subnormal
    {
        expo = 1-(pow(2,exp_b-1)-1);
        mant = float(stoi(s.substr(1+exp_b,sig_b), nullptr, 2))*pow(2, -sig_b);
    }
    return pow(-1, stoi(s.substr(0,1), nullptr, 2))*pow(2, expo)*mant;
}