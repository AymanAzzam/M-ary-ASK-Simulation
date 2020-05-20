import random
from math import pi, cos, sqrt
import numpy as np

##### Generate Random binary bits with size n #####
def randomBits(n):
    bits = []
    for i in range(n):  bits.append(random.randrange(2))
    return bits

##### The Mapper takes bits and return the signal to be transmitted #####
def mapper(bits):
    signal = []; E0 = 0

    while len(bits)%3 !=0: bits.append(0)

    ##### Calculate ai #####
    for i in range(0,len(bits),3):
        if(bits[i] == 1 and bits[i+1] == 1 and bits[i+2] == 0):     signal.append(-7)
        elif(bits[i] == 1 and bits[i+1] == 1 and bits[i+2] == 1):   signal.append(-5)
        elif(bits[i] == 1 and bits[i+1] == 0 and bits[i+2] == 1):   signal.append(-3)
        elif(bits[i] == 1 and bits[i+1] == 0 and bits[i+2] == 0):   signal.append(-1)
        elif(bits[i] == 0 and bits[i+1] == 0 and bits[i+2] == 0):   signal.append(1)
        elif (bits[i] == 0 and bits[i+1] == 0 and bits[i+2] == 1):  signal.append(3)
        elif(bits[i] == 0 and bits[i+1] == 1 and bits[i+2] == 1):   signal.append(5)
        else:                                                       signal.append(7)
    
    ##### Calculate E0 #####
    for i in signal:    E0 = E0 + i * i
    E0 = 3.0*len(signal)/E0
    
    ##### Calculate ai * sqrt(E0) #####
    for i in range(len(signal)):    signal[i] = signal[i] * sqrt(E0)

    return signal,E0

##### The Channel takes the transmitted signal to add AWGN to it #####
def channel(deviation,transmitted_signal):
    # 0 is the mean
    distorted_signal = transmitted_signal + np.random.normal(0,deviation, len(transmitted_signal))
    return distorted_signal

##### The DeMapper takes the received signal to retrieve the original bits #####
def demapper(E0,distorted_signal):
    received_bits = []
    
    ##### Getting The symbols #####
    for i in distorted_signal:
        x = i / sqrt(E0) 
        if(x <= -6):    received_bits.extend([1,1,0])
        elif(x <= -4):  received_bits.extend([1,1,1])
        elif(x <= -2):  received_bits.extend([1,0,1])
        elif(x <= 0):   received_bits.extend([1,0,0])
        elif(x <= 2):   received_bits.extend([0,0,0])
        elif (x <= 4):  received_bits.extend([0,0,1])
        elif(x <= 6):   received_bits.extend([0,1,1])
        else:           received_bits.extend([0,1,0])
    return received_bits

def main():
    BER = 0.0; deviation = 1

    ##### The bits to be transmitted #####
    bits = randomBits(12)
    print("Input bits : ",bits)

    ##### The transmitted signal for bits #####
    transmitted_signal,E0 = mapper(bits)
    print("Transmited Signal : ",transmitted_signal)
    ##### The signal after AWGN distortion #####
    distorted_signal = channel(deviation,transmitted_signal)
    print("Distorted Signal : ",distorted_signal)

    ##### The received bits #####
    received_bits = demapper(E0, distorted_signal)
    print("Recieved Signal : ",received_bits)

    #### Calculate BER #####
    for i in range(len(bits)):
        if(bits[i] == received_bits[i]):    BER = BER + 1
    BER = BER / len(bits)
    print("BER = ",BER)

##### Calling the main function #####
main()