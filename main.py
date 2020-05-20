import sys
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from math import pi, cos, sqrt,pow


##### Generate Random binary bits with size n #####
def randomBits(n):
    bits = []
    for i in range(n):  bits.append(random.randrange(2))
    return bits

##### The Mapper takes bits and return the signal to be transmitted #####
def mapper(E0,bits):
    signal = []; 

    while len(bits)%3 !=0: bits.append(0)

    ##### Calculate The Transmitted Signal #####
    for i in range(0,len(bits),3):
        if(bits[i] == 1 and bits[i+1] == 1 and bits[i+2] == 0):     signal.append(-7 * sqrt(E0))
        elif(bits[i] == 1 and bits[i+1] == 1 and bits[i+2] == 1):   signal.append(-5 * sqrt(E0))
        elif(bits[i] == 1 and bits[i+1] == 0 and bits[i+2] == 1):   signal.append(-3 * sqrt(E0))
        elif(bits[i] == 1 and bits[i+1] == 0 and bits[i+2] == 0):   signal.append(-1 * sqrt(E0))
        elif(bits[i] == 0 and bits[i+1] == 0 and bits[i+2] == 0):   signal.append(1 * sqrt(E0))
        elif (bits[i] == 0 and bits[i+1] == 0 and bits[i+2] == 1):  signal.append(3 * sqrt(E0))
        elif(bits[i] == 0 and bits[i+1] == 1 and bits[i+2] == 1):   signal.append(5 * sqrt(E0))
        else:                                                       signal.append(7 * sqrt(E0))

    return signal

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

##### To plot the result #####
def plot(x,y_simulated,y_theoretical):
    fig,ax=plt.subplots()
    ax.semilogy(x, y_simulated, '-')
    ax.set_xlabel("E0/N0")
    ax.set_ylabel("BER")
    ax.semilogy(x, y_theoretical, '--')
    plt.title("8-ary ASK Simulation")
    plt.show()

def main(bits_num):
    X_Axis = list();    BER_simulated = list();     BER_theoretical = list()

    ##### Calculate E0 #####
    E0 = 3 * 8 / ( (1 * 1 + 3 * 3 + 5 * 5 + 7 * 7) * 2 )

    ##### The bits to be transmitted #####
    bits = randomBits(bits_num)
    
    ##### The transmitted signal for bits #####
    transmitted_signal = mapper(E0,bits)

    for i in range(-4,17,2):
        X_Axis.append(i);   N0 = 1 / pow(10,i/10);  deviation = sqrt(N0/2)
        
        ##### Calculate BER Theoretical #####
        BER_theoretical.append(special.erfc(sqrt(E0/N0)) * 7 / 24)

        ##### The signal after AWGN distortion #####
        distorted_signal = channel(deviation,transmitted_signal)

        ##### The received bits #####
        received_bits = demapper(E0, distorted_signal)

        #### Calculate BER #####
        BER = 0.0
        for i in range(len(bits)):
            if(bits[i] != received_bits[i]):    BER = BER + 1
        BER = BER / len(bits)
        BER_simulated.append(BER)
    
    ##### Plotting the result #####
    plot(X_Axis,BER_simulated,BER_theoretical)

##### Calling the main function #####
if(len(sys.argv) != 2):
    print("Invalid Number of parameters, Enter only one Parameter (Number of decoded bits)")
else:
    bits_num = int(sys.argv[1])
    main(bits_num)